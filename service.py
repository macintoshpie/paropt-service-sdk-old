import os
import requests
import warnings

# ignore SSL warnings
# b/c server is currently using self signed cert, requests with arg valid=False raise a warning
# about the security of ignoring verifying the SSL cert
warnings.filterwarnings("ignore")

class Paropt:
  """Wrapper for paropt-service endpoints
  
  Parameters
  ----------
  domain : str
    domain of service
  port : int
    port of service
  session_cookie : str
    session cookie received after authenticating on website
  """
  def __init__(self, domain='localhost', port=8080, session_cookie=''):
    self.domain = domain
    self.port = port
    self.url = f'https://{self.domain}:{self.port}/api/v1'
    # TODO: use tokens
    self.session_cookie = session_cookie

    self.headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Cookie': f'session={self.session_cookie}'
    }

  def getOrCreateExperiment(self, experiment):
    return requests.post(url=f'{self.url}/experiments',
                         json=experiment,
                         headers=self.headers,
                         verify=False
                        )

  def runTrial(self, experiment_id, optimizer):
    return requests.post(url=f'{self.url}/experiments/{experiment_id}/trials',
                         json=optimizer,
                         headers=self.headers,
                         verify=False
                        )

  def getTrials(self, experiment_id):
    return requests.get(url=f'{self.url}/experiments/{experiment_id}/trials',
                        headers=self.headers,
                        verify=False
                       )

  def getRunningExperiments(self):
    return requests.get(url=f'{self.url}/experiments/running',
                        headers=self.headers,
                        verify=False
                       )
  def getFailedExperiments(self):
    return requests.get(url=f'{self.url}/experiments/failed',
                        headers=self.headers,
                        verify=False
                       )
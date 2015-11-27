# Copyright (c) 2015 HyperHQ Inc.
# Copyright 2013 dotCloud inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.



class HyperClient():
    def __init__(self, url):
        self.base_url = url

    def ping(self):
        result = self._result(self._get(self._url('/info')))

    def pods(self, all=True):
        #[id]
        return []

    def inspect_pods(self, pod_id):
        #[Config][Hostname]
        return {}

    def find_pod_by_uuid(self, uuid):
        #[id]
        return {}

    def load_image(self, image, path):
        return True

    def inspect_image(self, image):
        return {}

    def start(self, pod_id, binds=None, dns=None, privileged=False):
        return True

    def kill(self, pod_id):
        return True

    def remove_pod(self, pod_id, force=False):
        return True

    def stop(self, pod_id, timeout):
        return True

    def pause(self, pod_id):
        return True

    def unpause(self, pod_id):
        return True

    # ?
    def create_host_config(self, ?**args):
        return {}

    def create_pod(self, image_name, name, hostname, cpu_shares, network_disabled,environment, command, host_config):
        return True

    def get_pod_logs(self, pod_id):
        return "logs"

    def commit(self, pod_id, repository, tag):
        return True

    #def create_pod(self):
        #data = {
        #    "pod_file": "/path/to/podfile"
        #}

        #r = requests.post(self.url+"/pod/create?podArgs={0}".format(data))
        #return r.status_code, r.json()

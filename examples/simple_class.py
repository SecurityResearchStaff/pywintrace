########################################################################
# Copyright 2017 FireEye Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
########################################################################

import time
import etw


class MyETW(etw.ETW):

    def __init__(self):
        # define capture GUID
        guid = {'Some Provider': etw.GUID("{11111111-1111-1111-1111-111111111111}")}
        super().__init__(guid)

    def start(self, event_callback=None, task_name_filters=None, ignore_exists_error=True):
        # do pre-capture setup
        self.do_capture_setup()
        super().start(event_callback)

    def stop(self):
        super().stop()
        # do post-capture teardown
        self.do_capture_teardown()

    def do_capture_setup(self):
        # do whatever setup for capture here
        pass

    def do_capture_teardown(self):
        # do whatever for capture teardown here
        pass


def my_capture():
    # instantiate class
    capture = MyETW()
    # start capture
    capture.start(lambda x: print(x))
    # wait some time to capture data
    time.sleep(5)
    # stop capture
    capture.stop()


if __name__ == '__main__':
    my_capture()

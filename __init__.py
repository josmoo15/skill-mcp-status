# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests
__author__ = 'orsala'

LOGGER = getLogger(__name__)


class McpStatusSkill(MycroftSkill):
    def __init__(self):
        super(McpStatusSkill, self).__init__(name="McpStatusSkill")

    def get_mcp_waitings_status(self):

        data = requests.get("http://10.3.36.199/programs/waitings")
        if data.status_code == 200:
            return "There are not waitings"
        else:
            return "There are some waitings"

    def initialize(self):
        mcp_status = IntentBuilder("McpStatus"). \
            require("McpStatusword").build()
        self.register_intent(mcp_status, self.handle_mcp_status_intent)


    def handle_mcp_status_intent(self, message):
        print(self.get_mcp_waitings_status())
        self.speak_dialog("MCP Status")



    def stop(self):
        pass


def create_skill():
    return McpStatusSkill()

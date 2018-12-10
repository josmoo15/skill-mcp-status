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
import mcp_status
__author__ = 'orsala'

LOGGER = getLogger(__name__)


class McpStatusSkill(MycroftSkill):
    def __init__(self):
        super(McpStatusSkill, self).__init__(name="McpStatusSkill")

    def initialize(self):
        tell_me_the_mcp_status = IntentBuilder("TellMeTheMCPStatus"). \
            require("TellMeTheMCPStatusword").build()
        self.register_intent(tell_me_the_mcp_status, self.handle_tell_me_the_mcp_status_intent)


    def handle_tell_me_the_mcp_status_intent(self, message):
        self.speak_dialog(mcp_status.get_mcp_waitings_status())



    def stop(self):
        pass


def create_skill():
    return McpStatusSkill()

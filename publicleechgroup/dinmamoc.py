#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .get_cfg import get_config


class Commandi:
    LEECH = get_config(
        "COMMANDI_LEECH",
        "leech@manjirosano090_bot"
    )
    PURGE = get_config(
        "COMMANDI_PURGE",
        "purge@manjirosano090_bot"
    )
    YTDL = get_config(
        "COMMANDI_YTDL",
        "ytdl@manjirosano090_bot"
    )
    STATUS = get_config(
        "COMMANDI_STATUS",
        "status@manjirosano090_bot"
    )
    CANCEL = get_config(
        "COMMANDI_CANCEL",
        "cancel@manjirosano090_bot"
    )
    EXEC = get_config(
        "COMMANDI_EXEC",
        "exec@manjirosano090_bot"
    )
    EVAL = get_config(
        "COMMANDI_EVAL",
        "eval@manjirosano090_bot"
    )
    RENAME = get_config(
        "COMMANDI_RENAME",
        "rename@manjirosano090_bot"
    )
    UPLOAD = get_config(
        "COMMANDI_UPLOAD",
        "upload@manjirosano090_bot"
    )
    HELP = get_config(
        "COMMANDI_HELP",
        "help@manjirosano090_bot"
    )
    SAVETHUMBNAIL = get_config(
        "COMMANDI_SAVETHUMBNAIL",
        "savethumbnail@manjirosano090_bot"
    )
    CLEARTHUMBNAIL = get_config(
        "COMMANDI_CLEARTHUMBNAIL",
        "clearthumbnail@manjirosano090_bot"
    )
    GET_RCLONE_CONF_URI = get_config(
        "COMMANDI_GET_RCLONE_CONF_URI",
        "getrcloneconfuri@manjirosano090_bot"
    )
    UPLOAD_LOG_FILE = get_config(
        "COMMANDI_UPLOAD_LOG_FILE",
        "log@manjirosano090_bot"
    )

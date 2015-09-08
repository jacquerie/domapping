# -*- coding: utf-8 -*-
#
# This file is part of JsonSchema-to-ElasticMapping.
# Copyright (C) 2015 CERN.
#
# JsonSchema-to-ElasticMapping is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# JsonSchema-to-ElasticMapping is distributed in the hope that it will be
# useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with JsonSchema-to-ElasticMapping; if not, write to the Free Software
# Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Exceptions used in this package"""


class JsonSchemaSupportError(Exception):
    """Exception thrown when a json schema is not supported by a function."""
    def __init__(self, message, path, *args, **kwargs):
        super(JsonSchemaSupportError, self).__init__(*args, **kwargs)
        self.message = message
        self.path = path

    def __str__(self):
        return 'ERROR {0} IN {1}'.format(self.message, self.path)

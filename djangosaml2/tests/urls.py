# Copyright (C) 2012 Yaco Sistemas (http://www.yaco.es)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import django
from django.contrib import admin

from djangosaml2.views import (assertion_consumer_service, login, logout,
                               logout_service, metadata)

try:
    from django.conf.urls import include, url
    if django.VERSION < (1, 10):
        from django.conf.urls import patterns
# Fallback for Django versions < 1.4
except ImportError:
    from django.conf.urls.defaults import patterns, include, url

admin.autodiscover()

urlpatterns = [
    url(r'^login/$', login, name='saml2_login'),
    url(r'^acs/$', assertion_consumer_service, name='saml2_acs'),
    url(r'^logout/$', logout, name='saml2_logout'),
    url(r'^ls/$', logout_service, name='saml2_ls'),
    url(r'^metadata/$', metadata, name='saml2_metadata'),
    # this is needed for the tests
    url(r'^admin/', include(admin.site.urls)),
]

if django.VERSION < (1, 10):
    urlpatterns = patterns('', *urlpatterns)

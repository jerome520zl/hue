#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import url
from security import views
from security.api import hdfs, hive, sentry

urlpatterns = [
  url(r'^$', views.hive, name='index'),
  url(r'^hive$', views.hive, name='hive'),
  url(r'^hive2$', views.hive2, name='hive2'),
  url(r'^solr$', views.solr, name='solr'),
  url(r'^hdfs$', views.hdfs, name='hdfs'),
]


urlpatterns += [
  url(r'^api/hdfs/list(?P<path>/.*)$', hdfs.list_hdfs, name='list_hdfs'),
  url(r'^api/hdfs/get_acls$', hdfs.get_acls, name='get_acls'),
  url(r'^api/hdfs/update_acls', hdfs.update_acls, name='update_acls'),
  url(r'^api/hdfs/bulk_delete_acls', hdfs.bulk_delete_acls, name='bulk_delete_acls'),
  url(r'^api/hdfs/bulk_add_acls', hdfs.bulk_add_acls, name='bulk_add_acls'),
  url(r'^api/hdfs/bulk_sync_acls', hdfs.bulk_sync_acls, name='bulk_sync_acls'),
]


urlpatterns += [
  url(r'^api/hive/fetch_hive_path', hive.fetch_hive_path, name='fetch_hive_path'),

  url(r'^api/hive/list_sentry_roles_by_group', hive.list_sentry_roles_by_group, name='list_sentry_roles_by_group'),
  url(r'^api/hive/list_sentry_privileges_by_role', hive.list_sentry_privileges_by_role, name='list_sentry_privileges_by_role'),
  url(r'^api/hive/list_sentry_privileges_for_provider$', hive.list_sentry_privileges_for_provider, name='list_sentry_privileges_for_provider'),
  url(r'^api/hive/list_sentry_privileges_by_authorizable', hive.list_sentry_privileges_by_authorizable, name='list_sentry_privileges_by_authorizable'),
  url(r'^api/hive/create_sentry_role', hive.create_sentry_role, name='create_sentry_role'),
  url(r'^api/hive/update_role_groups', hive.update_role_groups, name='update_role_groups'),
  url(r'^api/hive/drop_sentry_role', hive.drop_sentry_role, name='drop_sentry_role'),
  url(r'^api/hive/create_role$', hive.create_role, name='create_role'),
  url(r'^api/hive/save_privileges$', hive.save_privileges, name='save_privileges'),
  url(r'^api/hive/bulk_delete_privileges', hive.bulk_delete_privileges, name='bulk_delete_privileges'),
  url(r'^api/hive/bulk_add_privileges', hive.bulk_add_privileges, name='bulk_add_privileges'),
  url(r'^api/hive/grant_privilege', hive.grant_privilege, name='grant_privilege'),

  # Unused: API is for blind bulk operations
  url(r'^api/hive/rename_sentry_privilege', hive.rename_sentry_privilege, name='rename_sentry_privilege'),
]


# Generic API V2
urlpatterns += [
  url(r'^api/sentry/fetch_authorizables', sentry.fetch_authorizables, name='fetch_authorizables'),

  url(r'^api/sentry/list_sentry_roles_by_group', sentry.list_sentry_roles_by_group, name='list_sentry_roles_by_group'),
  url(r'^api/sentry/list_sentry_privileges_by_role', sentry.list_sentry_privileges_by_role, name='list_sentry_privileges_by_role'),
  url(r'^api/sentry/list_sentry_privileges_for_provider$', sentry.list_sentry_privileges_for_provider, name='list_sentry_privileges_for_provider'),
  url(r'^api/sentry/list_sentry_privileges_by_authorizable', sentry.list_sentry_privileges_by_authorizable, name='list_sentry_privileges_by_authorizable'),
  url(r'^api/sentry/create_sentry_role', sentry.create_sentry_role, name='create_sentry_role'),
  url(r'^api/sentry/update_role_groups', sentry.update_role_groups, name='update_role_groups'),
  url(r'^api/sentry/drop_sentry_role', sentry.drop_sentry_role, name='drop_sentry_role'),
  url(r'^api/sentry/create_role$', sentry.create_role, name='create_role'),
  url(r'^api/sentry/save_privileges$', sentry.save_privileges, name='save_privileges'),
  url(r'^api/sentry/bulk_delete_privileges', sentry.bulk_delete_privileges, name='bulk_delete_privileges'),
  url(r'^api/sentry/bulk_add_privileges', sentry.bulk_add_privileges, name='bulk_add_privileges'),
  url(r'^api/sentry/grant_privilege', sentry.grant_privilege, name='grant_privilege'),

  # Unused: API is for blind bulk operations
  url(r'^api/sentry/rename_sentry_privilege', sentry.rename_sentry_privilege, name='rename_sentry_privilege'),
]

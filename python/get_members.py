# Copyright  2020  Edoardo Riggio
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

# Mailchimp module (used to manage the subscribers)
from mailchimp3 import MailChimp

def get_members():
    """
    Create a dictionary of subscribers, which has key that is the subscriber's email and the
    value that is a list of countries selected by the user when registering

    Returns:
        dict: a dictionary of subscribers
    """
    client = MailChimp('72e1014164ec892ea15f5f0f5ae03c79-us19')
    members = client.lists.members.all('c4abf5aa93', get_all=True, fields="members.email_address")['members']
    countries = client.lists.members.all('c4abf5aa93', get_all=True, fields="members.merge_fields")['members']

    subscribers : {str: list} = {}

    for member, country in zip(members, countries):
        if len(country['merge_fields']['COUNTRY']) != 0:
            subscribers[member['email_address']] = country['merge_fields']['COUNTRY'].split(', ')

    return subscribers
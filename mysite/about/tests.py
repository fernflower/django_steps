from django.test import TestCase
from django.core.urlresolvers import reverse
from about.models import Member


class MemberViewsTest(TestCase):
    def test_id_and_alias_get(self):
        # make sure that /about/member/1 == /about/member/member_alias
        member = Member(name="Samwell Tarly", alias="slayer",
                        info="I am a craven")
        member.save()
        response_1 = self.client.get(reverse("about:member", args=(member.id,)))
        response_2 = self.client.get(reverse("about:member",
                                     args=(member.alias,)))
        for response in [response_1, response_2]:
            self.assertContains(response, member.info)
        # if there is no such page, no 404 should be received, 200 OK with neat
        # calming text that there is no member data yet
        response = self.client.get(reverse("about:member",
                                   args=("no_such_member",)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No member data yet")

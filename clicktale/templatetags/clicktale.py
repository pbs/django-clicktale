from django import template
from django.conf import settings

from django.template import Context, loader


register = template.Library()


def do_get_clicktale(parser, token):
    tag_name = token.split_contents()[0]
    template_name = 'clicktale/%s_template.html' % tag_name

    try:
        project_id = settings.CLICKTALE_PROJECT_ID
        recording_ratio = settings.CLICKTALE_RECORDING_RATIO
        partition_id = settings.CLICKTALE_PARTITION_ID
        ajax_enabled = settings.CLICKTALE_AJAX_ENABLED
        return ClickTaleNode(
            project_id=project_id, recording_ratio=recording_ratio,
            partition_id=partition_id, ajax_enabled=ajax_enabled,
            template_name=template_name
        )

    except AttributeError:
        # If not configured properly the templatetag
        # won't stop the application
        return ClickTaleNode()


class ClickTaleNode(template.Node):

    def __init__(self, project_id=None, recording_ratio=0,
                 partition_id=None, ajax_enabled=False,
                 template_name=None):
        self.project_id = project_id
        self.recording_ratio = recording_ratio
        self.partition_id = partition_id
        self.ajax_enabled = ajax_enabled
        self.template_name = template_name

    def render(self, context):
        unconfigured_msg = '<!-- ClickTale configuration not available -->'

        request = context['request']
        if request.is_ajax() and not self.ajax_enabled:
            return unconfigured_msg

        if self.project_id and self.partition_id:
            t = loader.get_template(self.template_name)
            c = Context({
                'project_id': self.project_id,
                'recording_ratio': self.recording_ratio,
                'partition_id': self.partition_id
            })
            return t.render(c)

        return unconfigured_msg


register.tag('clicktale_top', do_get_clicktale)
register.tag('clicktale_bottom', do_get_clicktale)


__author__ = 'sparky'
from django.views.generic import TemplateView


class BootsView(TemplateView):
    template_name = None
    container_type = None

    def render(self, elements):

        if self.template_name is None:
            msg = 'template_name is not defined'
            raise AttributeError(msg)
        if self.container_type is None:
            msg = 'container_type is not defined'
            raise AttributeError(msg)

        elements.update({'container_type': self.container_type})
        return self.render_to_response(elements)


class BootsFixedContainerView(BootsView):
    container_type = 'container'


class BootsFlowContainerView(BootsView):
    container_type = 'flow-container'
import unittest

from .test_tosca_base import TestToscaBase


class TestNginxLifecycle(TestToscaBase):

    def test(self):
        file = 'data/examples/nginx-lifecycle/nginx-lifecycle.yaml'
        up = self.o.read_plan_file(
            'data/examples/nginx-lifecycle/nginx-lifecycle.up.plan'
        )
        down = self.o.read_plan_file(
            'data/examples/nginx-lifecycle/nginx-lifecycle.down.plan'
        )
        self.assert_up_start(file, up)
        self.assert_down(file, down)


if __name__ == '__main__':
    unittest.main()

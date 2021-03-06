"""Bare bones test for rgb model in i3d.

"""

import mxnet as mx

import i3d

ctx = mx.cpu()
_IMAGE_SIZE = 224
_NUM_CLASSES = 4
_SAMPLE_VIDEO_FRAMES = 79
_BATCH_SIZE = 1
_NUM_CHANNELS = 3

def _test_model(net, ctx, x):
    net.initialize()
    net.collect_params().reset_ctx(ctx)
    net(x)
    mx.nd.waitall()


def test():
    # 3 channels for rgb model
    # NCDHW layout in Gluon
    x = mx.random.uniform(shape=(_BATCH_SIZE, _NUM_CHANNELS, _SAMPLE_VIDEO_FRAMES, _IMAGE_SIZE, _IMAGE_SIZE), ctx=ctx)
    net = i3d.i3d()
    _test_model(net, ctx, x)


if __name__ == '__main__':
    import nose

    nose.runmodule()

from static.cyclegan.options.base_options import BaseOptions

class ArgParseManual():
    def __init__(self):
        self.aspect_ratio = 1.0
        self.phase = 'test'
        self.isTrain = False
        # self.eval  'store_true'
        # self.num_test = 1
        # self.results_dir = 'static/results/'

        # From Base-args
        self.dataroot = 'static/cyclegan/datasets/dataset/testA'
        self.name = 'selfie2anime'
        self.gpu_ids = 'cpu'
        self.checkpoints_dir = 'static/cyclegan/pre'
        self.model = 'test'
        self.input_nc = 3
        self.output_nc = 3
        self.ngf = 64
        self.ndf = 64
        self.netD = 'basic'
        self.netG = 'resnet_9blocks'
        self.n_layers_D = 3
        self.norm = 'instance'
        self.init_type = 'normal'
        self.init_gain = 0.2
        self.no_dropout = False
        # self.dataset_mode = 'unaligned'
        self.direction = 'AtoB'
        self.serial_batches = 'store_true'
        self.num_threads = 4
        self.batch_size = 1
        self.load_size = 286
        self.crop_size = 256
        self.max_dataset_size = float('inf')
        self.preprocess = 'resize_and_crop'
        self.no_flip = True
        self.display_winsize = 256
        self.epoch = 'latest'
        self.load_iter = 0
        self.verbose = True
        self.suffix = ''
        self.initialized = True
        self.dataset_mode = 'single'
        self.model_suffix = ''

class TestOptions(BaseOptions):
    """This class includes test options.

    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)  # define shared options
        #parser.add_argument('--dataroot', required=True, default='datasets/dataset/testA')
        parser.add_argument('--results_dir', type=str, default='static/results/', help='saves results here.')
        parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio of result images')
        parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        # Dropout and Batchnorm has different behavioir during training and test.
        parser.add_argument('--eval', action='store_true', help='use eval mode during test time.')
        parser.add_argument('--num_test', type=int, default=1, help='how many test images to run')

        # To avoid cropping, the load_size should be the same as crop_size
        #parser.set_defaults(load_size=parser.get_default('crop_size'))
        #parser.set_defaults(dataroot=parser.get_default('dataroot'))
        #parser.set_defaults(no_dropout=parser.get_default('no_dropout'))
        self.isTrain = False
        return parser

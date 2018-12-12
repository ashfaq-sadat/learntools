# See also examples/example_track/example_meta.py for a longer, commented example
track = dict(
    author_username='dansbecker',
    course_name='Deep Learning',
    course_url='https://www.kaggle.com/learn/deep-learning'
)

lessons = [ {'topic': topic_name} for topic_name in
                    [
		 	'Intro to Deep Learning and Computer Vision',
			'Building Models from Convolutions',
			'TensorFlow programming',
			'Transfer Learning',
			'Data Augmentation',
			'A Deeper Understanding of Deep Learning',
			'Deep Learning from Scratch',
			'Dropout and Strides for Larger Models',	
			]
            ]

notebooks = [
    dict(
        filename='tut1_intro.ipynb',
        lesson_idx=0,
        type='tutorial',
        ),
    dict(
	filename='ex1_convolutions.ipynb',
	lesson_idx=0,
	type='exercise',
	scriptid=499266,
	dataset_sources = ["keras/resnet50"],
	competition_sources = ["dog-breed-identification"],
	),
    dict(
        filename='tut2_building_models_from_convolutions.ipynb',
        lesson_idx=1,
        type='tutorial',
        ),
    dict(
        filename='tut3_programming_tf_and_keras.ipynb',
        lesson_idx=2,
        type='tutorial',
	dataset_sources = ["keras/resnet50"],
	competition_sources = ["dog-breed-identification"],
    ),
    dict(
        filename='ex3_programming_tf_and_keras.ipynb',
        lesson_idx=2,
        type='exercise',
	scriptid=521452,
	dataset_sources = [
	    "keras/resnet50",
	    "keras/vgg16",
	    "dansbecker/hot-dog-not-hot-dog"
	  ],
    ),
    dict(
        filename='tut4_transfer_learning.ipynb',
        lesson_idx=3,
        type='tutorial',
	dataset_sources = [
	    "keras/resnet50",
	    "dansbecker/urban-and-rural-photos"
	  ],
    ),
    dict(
        filename='ex4_transfer_learning.ipynb',
        lesson_idx=3,
        type='exercise',
	scriptid=532365,
	dataset_sources = [
	    "keras/resnet50",
	    "dansbecker/dogs-gone-sideways"
	  ],
    ),
    dict(
        filename='tut5_data_augmentation.ipynb',
        lesson_idx=4,
        type='tutorial',
	dataset_sources = [
	    "keras/resnet50",
	    "dansbecker/urban-and-rural-photos",
	  ],
    ),
    dict(
        filename='ex5_data_augmentation.ipynb',
        lesson_idx=4,
        type='exercise',
	scriptid=536195,
       	dataset_sources = [
	    "keras/resnet50",
	    "dansbecker/dogs-gone-sideways"
	  ],
 ),
    dict(
        filename='tut6_deep_understanding.ipynb',
        lesson_idx=5,
        type='tutorial',
        ),
    dict(filename='tut7_dl_from_scratch.ipynb',
        lesson_idx=6,
        type='tutorial',
	dataset_sources = ['zalando-research/fashionmnist'],
	competition_sources=['digit-recognizer'],
        ),
    dict(
        filename='ex7_from_scratch.ipynb',
        lesson_idx=6,
        type='exercise',
        scriptid=574269,
	competition_sources=['digit-recognizer'],
	dataset_sources = ['zalando-research/fashionmnist'],
        ),
    dict(
        filename='tut8_dropout_and_strides.ipynb',
        lesson_idx=7,
        type='tutorial',
	competition_sources=['digit-recognizer'],
	dataset_sources = ['zalando-research/fashionmnist'],
        ),
    dict(
        filename='ex8_dropout_strides.ipynb',
        lesson_idx=7,
        type='exercise',
	scriptid=663261,
	competition_sources=['digit-recognizer'],
    dataset_sources = ['zalando-research/fashionmnist'],
        ),
]
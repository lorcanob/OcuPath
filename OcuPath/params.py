# List of 8 potential multicategory targets
TARGET_LIST = ['Normal (N)',
               'Diabetes (D)',
               'Glaucoma (G)',
               'Cataract (C)',
               'Age related Macular Degeneration (A)',
               'Hypertension (H)',
               'Pathological Myopia (M)',
               'Other diseases/abnormalities (O)']

# Information to be extracted from full_df to be used for left eye
LEFT_INFO = [
    'Patient Age',
    'Patient Sex',
    'Left-Fundus',
    'Left-Diagnostic Keywords',
]

# Information to be extracted from full_df to be used for right eye
RIGHT_INFO = [
    'Patient Age',
    'Patient Sex',
    'Right-Fundus',
    'Right-Diagnostic Keywords',
]

# Mapper to rename right_df columns to merge with left_df
RIGHT_MAPPER = {
    'Right-Fundus': 'Image',
    'Right-Diagnostic Keywords': 'Diagnostic Keywords'
}

# Mapper to rename left_df columns to merge with right_df
LEFT_MAPPER = {
    'Left-Fundus': 'Image',
    'Left-Diagnostic Keywords': 'Diagnostic Keywords'
}

# Mapper to rename human_df columns to model_df columns
MODEL_MAPPER = {
    'Patient Sex': 'Patient Male',
    'Eye': 'Right Eye'
}

# Mapper to binary encode Patient Sex
SEX_MAPPER = {
    'Female': 0,
    'Male': 1
}

# Mapper to binary encode Patient Eye
EYE_MAPPER = {
    'Left': 0,
    'Right': 1
}

COLLAPSER = {
    'normal fundus': 'Normal',
    'diabetic retinopathy': 'Diabetes',
    'mild nonproliferative retinopathy': 'Diabetes',
    'moderate nonproliferative retinopathy': 'Diabetes',
    'proliferative diabetic retinopathy': 'Diabetes',
    'severe nonproliferative retinopathy': 'Diabetes',
    'severe proliferative diabetic retinopathy': 'Diabetes',
    'glaucoma': 'Glaucoma',
    'suspected glaucoma': 'Glaucoma',
    'cataract': 'Cataract',
    'dry age-related macular degeneration': 'Age-related Macula Degeneration',
    'wet age-related macular degeneration': 'Age-related Macula Degeneration',
    'hypertensive retinopathy': 'Hypertension',
    'myopia retinopathy': 'Myopia',
    'myopic maculopathy': 'Myopia',
    'pathological myopia': 'Myopia',
    'atrophic change': 'Other',
    'atrophy': 'Other',
    'branch retinal artery occlusion': 'Other',
    'branch retinal vein occlusion': 'Other',
    'central retinal artery occlusion': 'Other',
    'central retinal vein occlusion': 'Other',
    'central serous chorioretinopathy': 'Other',
    'chorioretinal atrophy': 'Other',
    'chorioretinal atrophy with pigmentation proliferation': 'Other',
    'congenital choroidal coloboma': 'Other',
    'depigmentation of the retinal pigment epithelium': 'Other',
    'drusen': 'Other',
    'epiretinal membrane': 'Other',
    'epiretinal membrane over the macula': 'Other',
    'fundus laser photocoagulation spots': 'Other',
    'glial remnants anterior to the optic disc': 'Other',
    'idiopathic choroidal neovascularization': 'Other',
    'intraretinal microvascular abnormality': 'Other',
    'laser spot': 'Other',
    'macular coloboma': 'Other',
    'macular hole': 'Other',
    'macular epiretinal membrane': 'Other',
    'maculopathy': 'Other',
    'morning glory syndrome': 'Other',
    'myelinated nerve fibers': 'Other',
    'old branch retinal vein occlusion': 'Other',
    'old central retinal vein occlusion': 'Other',
    'old chorioretinopathy': 'Other',
    'optic disc edema': 'Other',
    'optic discitis': 'Other',
    'optic disk epiretinal membrane': 'Other',
    'oval yellow-white atrophy': 'Other',
    'peripapillary atrophy': 'Other',
    'pigment epithelium proliferation': 'Other',
    'pigmentation disorder': 'Other',
    'post retinal laser surgery': 'Other',
    'refractive media opacity': 'Other',
    'retina fold': 'Other',
    'retinal pigmentation': 'Other',
    'retinal vascular sheathing': 'Other',
    'retinitis pigmentosa': 'Other',
    'retinochoroidal coloboma': 'Other',
    'silicone oil eye': 'Other',
    'spotted membranous change': 'Other',
    'suspected abnormal color of optic disc': 'Other',
    'suspected retinal vascular sheathing': 'Other',
    'tessellated fundus': 'Other',
    'vitreous degeneration': 'Other',
    'wedge white line change': 'Other'
}

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

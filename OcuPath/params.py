TARGET_LIST = ['Normal (N)',
               'Diabetes (D)',
               'Glaucoma (G)',
               'Cataract (C)',
               'Age related Macular Degeneration (A)',
               'Hypertension (H)',
               'Pathological Myopia (M)',
               'Other diseases/abnormalities (O)']

LEFT_INFO = [
    'Patient Age',
    'Patient Sex',
    'Left-Fundus',
    'Left-Diagnostic Keywords',
]

RIGHT_INFO = [
    'Patient Age',
    'Patient Sex',
    'Right-Fundus',
    'Right-Diagnostic Keywords',
]

RIGHT_MAPPER = {
    'Right-Fundus': 'Image',
    'Right-Diagnostic Keywords': 'Diagnostic Keywords'
}

LEFT_MAPPER = {
    'Left-Fundus': 'Image',
    'Left-Diagnostic Keywords': 'Diagnostic Keywords'
}

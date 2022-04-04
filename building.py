import streamlit as st
from help_text import help
import datetime
import pandas as pd

destination = [
    ' ',
    'Residential area',
    'Beach',
    'Business area Barcadera',
    'Business area San Nicolas',
    'Tourist area East coast',
    'Tourist area West coast',
    'Nature and landscape',
    'Nature reserve',
    'Naval area',
    'Urban residential area',
    'Rural area',
    'Airport',
    'Center Oranjestad'
]

designation = [
    ' ',
    'LG1',
    'LG2',
    'LG3',
    'Economic interest',
    'Transition area',
    'Malmok',
    'Sero Colorado',
    'Landscape integration',
    'High rise',
    'Low rise',
    'North point',
    'Tourist interest',
    'Office zone',
    'Kite surf',
    'Parkieten bos',
    'Golf course',
    'Sewage treatment plant'
]

roofs = [
    'Bonnet roof',
    'Butterfly roof',
    'Clerestory roof',
    'Combination roof',
    'Curved roof',
    'Dome roof',
    'Dormer roof',
    'Flat roof',
    'Gable roof',
    'Gambrel roof',
    'Hexagonal roof',
    'Hip roof',
    'Jerkinhead roof',
    'Mansard roof',
    'Saltbox roof',
    'Shed roof',
    'Lean-to/Skillion roof',
    'Sawtooth',
    'Pyramid',
    'Pent',
]

roofing = {
    'Shingles': [
        'Asphalt',
        'Fibre Cement',
        'Metal',
        'Slate'
        'Synthetic',
        'Wood Shakes',
    ],
    'Tiles': [
        'Clay',
        'Concrete',
        'Solar',
        'Synthetic'
    ],
    'Panels': [
        'Standing Seam Metal',
        'Flat Seam Metal',
        'Corrugated Asphalt',
        'Corrugated Fiber Cement',
        'Corrugated Fiberglass',
        'Corrugated Metal',
        'Corrugated PVC',
        'Insulated Roof',
        'Metal Tile Roofing',
        'Ribbed Metal',
        'Stone-Coated Steel',
        '“Tin” Roofs'
    ],
    'Bitumen-Based Roofing': [
        'Built-Up Roofing (BUR)',
        'Modified Bitumen Roofing',
        'Roll Roofing'
    ],
    'Single-Ply Membrane Roofing': [
        'CPE Membrane (Chlorinated Polyethylene)',
        'CSPE or “Hypalon” Membrane (Chlorosulfonated Polyethylene)',
        'EPDM Membrane (Ethylene Propylene Diene Monomer)',
        'KEE/PVC Membrane (Ketone Ethylene Ester, Polyvinyl Chloride)',
        'PIB Membrane (Polyisobutylene)',
        'PVC Membrane (Polyvinyl Chloride)',
        'TPO Membrane (Thermoplastic Polyolefin)'
    ]
}

floor_finishes = [
    ' ',
    'Hardwood',
    'Concrete',
    'Laminate',
    'Linoleum',
    'Vinyl',
    'Marble',
    'Granite',
    'Slate',
    'Ceramic',
    'Porcelain',
    'Glass',
    'Vitrified',
    'Mosaic',
    'Cork',
    'Terrazzo',
    'Pebble',
    'Limestone',
    'Travertine',
    'Bamboo',
    'Onyx',
    'Granite',
    'Travertine',
    'Natrual slate',
    'Sandstone',
    'Carpet',
]

wall_material = [
    ' ',
    'Plywood',
    'Cinder blocks',
    'Concrete blocks',
    'Cement blocks',
    'Glass',
    'Wood',
    'Cork',
    'Steel sheets',
    'Peg board',
    'Sheetrock',
    'Terracotta',
]

wall_finish = [
    ' ',
    'Drywall',
    'Wood planks',
    'Veneer plaster',
    'Plywood or Sheetwood',
    'Texture wall panels',
    'Brick and masonry',
    'Exposed concrete block',
    'Cement board',
    'Pegboard',
    'Cork board',
    'Wahoo walls',
    'Cement plaster',
    'Lath and plaster',
    'Concrete veneer',
    'Lime plaster',
    'Reinforced fiberglass panels',
    'Gypsum panels',
    'Corrugated metal',
    'Vinyl siding',
]

window_type = [
    ' ',
    'Single hung',
    'Double hung',
    'Arched',
    'Awning',
    'Bay',
    'Bow',
    'Casement',
    'Egress',
    'Garden',
    'Glass block',
    'Hopper',
    'Jalousie',
    'Picture',
    'Round circle',
    'Skylight',
    'Sliding',
    'Storm',
    'Transom',
    'Custom',
]

frame_materials = [
    ' ',
    'Wood',
    'Vinyl',
    'Fiberglass',
    'Aluminium',
    'Wood clad',
    'Composite',
    'UPVC',
]

countertops = [
    ' ',
    'Ceremic tile',
    'Concrete',
    'Granite',
    'Laminate',
    'Marble',
    'Quartz',
    'Soapstone',
    'Stainless steel',
    'Wood',
    'Engineered stone material',
]

cabinet_material = [
    ' ',
    'Laminate',
    'Particleboard',
    'Fibreboard',
    'Plywood',
    'Wood',
    'Hardwood',
    'Wood veneer',
    'Stainless steel',
    'Rubberwood',
]

solar_type = [
    'Monocrystalline',
    'Polycrystalline solar',
    'Thin-film',
    'Biohybrid',
    'Cadmium telluride',
    'Concentrated PV',
    'Unspecified',
]

garden_buildings = [
    'Cabanas',
    'Garden office',
    'Gloriette',
    'Greenhouse',
    'Nymphaea',
    'Orangeries',
    'Pavilions',
    'Jacuzzi',
    'Pool (inground)',
]

eds = {
    'Porch': ['Open', 'Front entry', "Farmer's", 'Back', 'Detached', 'Screened', 'Rain', 'Portico', 'Lanai'],
    'Balcony': ['True', 'Faux', 'False', 'Mezzanine'],
    'Verandah': ['Flat roof', 'Curved roof', 'Gazebo', 'Pergola', 'Sunroof', 'Gable roof'],
    'Patio': {'material': ['Concrete', 'Asphalt', 'Pavers', 'Brick', 'Blue stone', 'Lime stone', 'Gravel', 'Other']},
    # 'Deck': {'style': ['Attached', 'Detached', 'Wraparound', 'Multi-level', 'Side-yard', 'Swimming pool', 'Entryway', 'Rooftop'],
    #         'material': ['Bamboo', 'Redwood', 'Cedar', 'Pressure treated wood', 'Ipe', 'Modified wood', 'Composite', 'Vinyl', 'PVC', 'Aluminium', 'Other']
    # },
}

parking = [
    ' ',
    'On-street',
    'Off-street',
    'Breezeway',
    'Carport',
    'Detached garage',
    'Attached garage',
    'Indoor',
    'Parkade',
    'Underground',
    'Outdoor stalls',
    'Parking pad',
]

ceiling_type = [
    '',
    'False/Suspended',
    'Shed ceiling',
    'Tray ceiling',
    'Flat ceiling',
    'Tin ceiling',
    'Coffered ceiling',
    'Cathedral/Valuted',
    'Domed ceiling',
    'Cove ceiling',
    'Beamed ceiling',
    'Shadow-lined ceiling',
    'High ceiling',
    'Exposed ceiling',
    'Acoustic ceiling',
]

ceiling_material = [
    '',
    'Drywall',
    'Plaster',
    'Metal',
    'Wooden',
    'Timber',
    'Fiberglass tile',
]

door_type = [
    ' ',
    'Battened/Ledge door',
    'Hinged door',
    'Dutch door',
    'Pocket door',
    'Roller door',
    'Bifold door',
    'Sliding door',
    'Pivot door',
    'French door',
    'Louvered door',
    'Swing door',
    'Collapsible door',
    'Rolling shutters',
    'Revolving door',
]

door_material = [
    ' ',
    'Bamboo',
    'Glass',
    'Aluminium',
    'Fibre glass',
    'Fibre-reinforced plastic',
    'Steel',
    'Wood panels',
]

foundation_type = [
    'Concrete slab',
    'Reinforced concrete',
    'Full basement',
    'Daylight basement',
    'Pier and beam crawlspace',
    'Footing and stem wall crawlspace',
]

load_bearing = [
    'Precast concrete wall',
    'Retaining wall',
    'Masonry wall',
    'Engineering brick wall',
    'Stone wall',
    'Pre penalized load bearing metal stud wall',
]

partitioning_material = [
    'Brick partitions wall',
    'Clay brick partition wall',
    'Glass partitions wall',
    'Concrete partitions wall',
    'Plaster slab partition wall',
    'Metal lath partition wall',
    'A.C. sheet or G.I. sheet',
    'Wood-wool partition wall',
    'Timber partitions',
]

floor_trans = {
    -1: 'Basement',
    0: 'Ground floor',
    1: '1st floor',
    2: '2nd floor',
    3: '3rd Floor'
}

fencing_material = [
    'No fencing',
    'Aluminium',
    'Wood',
    'PVC',
    'Wrought Iron',
    'Vinyl',
    'Chain link',
    'Electric',
    'Cacti',
    'Concrete bricks',
    'Wooden beams',
    'Bricks',
    'Hollow bricks',
    'Steel',
    'Natural stone',
]

outdoor_flooring = [
    'Hardwood deck',
    'Composite deck',
    'Outdoor carpeting',
    'Ceramic tiles',
    'Natural stone',
    'Brick & Concrete pavers',
    'Rubber tiles',
    'Artificial grass',
    'Concrete',
    'Gravel',
    'Ground-cover plants',
    'Foam tiles',
    'Artificial grass tiles',
    'Plastic tiles',
    'Luxury vinyl plank',
    'Landscaping'
]

recreation = [
    'Swimming pool',
    'Barbecue area',
    'Firepit',
    'Gym/Fitness center',
    'Yoga/Cardio room',
    'Community clubhouse',
    'Playground',
    'Rooftop lounge area',
    'Community garden',
    'Media room',
    'Common area',
]

pet_amenities = [
    'Pet-friendly units',
    'Pet washing station',
    'Dog parks',
]

parking_amenities = [
    'Secured garage',
    'Assigned parking space',
    'Carport',
    'Covered parking space',
    'Access to public transport',
    'Electric vehicle charging stations',
    'Guest parking',
    'Bike storage',
    'Bike repair centers',
]

community_amenities = [
    'Laundry facilities',
    'Laundry services',
    'Package lockers',
    'Gated community',
    'Security guards/doormen',
    'Community events/classes',
    'Extra storage space',
    'Online rent payments',
    'Online maintenance requests'
]

in_unit_amenities = [
    'In-unit laundry',
    'Air conditioning',
    'Storage space or Large closets',
    'Patio or Balcony space',
    'Dishwasher',
    'Engery-efficient appliances',
    'High-speed Internet access',
    'Large windows with natural light',
    'Views',
    'Fireplace',
    'Hardwood floors'
]

distinctive_features = [
    'Vegetable garden',
    'Sand volleyball court',
    'Tennis court',
    'Basketball court',
    'Miniture golf course',
    'Space for lawn bowling or bocci ball',
    'Outdoor fitness center',
    'Gazebo',
    'Rock garden',
    'Golf course',
]

commercial_building = {
    'Office': 'Office building',
    'Retail': ['Retail store', 'Shopping centre', 'shop'],
    'Industrial': ['Factory', 'Warehouse', 'Flex industrial'],
    'Multifamily': ['High-rise', 'Mid-rise', 'Garden-style', 'Walk-up', 'Manufactured housing community', 'Special-purpose housing'],
    'Hotel': ['Limited-service', 'Full-service', 'Boutique', 'Casino', 'Extended-stay', 'Resort'],
    'Leisure': ['Restaurant', 'Cafe', 'Sport facility'],
    'Healthcare': ['Medical centre', 'Hospital', 'Nursing homes'],
    'Special purpose': ['Amusement park', 'Church', 'Self-storage', 'Bowling alley', 'Other']
}


def general_info(type):

    with st.expander('GENERAL'):

        global lst
        global keys
        dct = {'general': {}}

        # Prices
        col1, col2 , col3 = st.columns([1, 1, 1])
        dct['general'].update({
                'asking_price':         col1.text_input('Asking price (Afl.)', key=next(keys)),
                'minimum_offer':        col2.text_input('Minimum acceptable offer (Afl.)', help=help['minimum_acceptable_offer'], key=next(keys)),
                'previous_transaction': col3.text_input('Previous Transaction (Afl)', help=help['previous_transaction'], key=next(keys))
        })

        # Dimensions
        columns = {}
        count = 1
        columns['col1'], columns['col2'], columns['col3'] = st.columns([1, 1, 1])
        if type != 'Condominium' and type != 'Apartment':
            dct['general'].update({
                'lot_area':         columns[f'col{count}'].text_input('Lot area (m2)', key=next(keys))
            }); count += 1

        if type != 'Land':
            dct['general'].update({
                'living_space':     columns[f'col{count}'].text_input('Living space (m2)', help=help['construction_size'], key=next(keys))
            }); count += 1

        # Images
        st.write(' ')
        st.write('**Images**')
        dct['general'].update({
                'images': st.file_uploader('Upload main image of Property', type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
        })

        return dct

def location():

    global keys
    dct = {'location': {}}

    with st.expander('LOCATION'):

        # Cadastral
        col1, col2 = st.columns([1, 1])
        dct['location'].update({
            'c-number': col1.text_input('Cadastral number / C-number', help=help['cadastral'], key=next(keys))
        })

        # Address
        col1, col2, col3, col4  = st.columns([6, 1.2, 1, 1])
        dct['location'].update({
            'street_name':  col1.text_input('Street name', key=next(keys)),
            'house_number': col2.text_input('Number', key=next(keys)),
            'suffix':       col3.text_input('Suffix', key=next(keys)),
            'unit':         col4.text_input('Unit', key=next(keys))
        })

        col1, col2, col3 = st.columns([2, 2, 1])
        dct['location'].update({
            'neighbourhood':    col1.text_input('Neighbourhood', key=next(keys)),
            'district':         col2.text_input('District', key=next(keys)),
            'gac':              col3.text_input('GAC', help=help['gac'], key=next(keys))
        })

        # Map
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        st.subheader('Map')
        st.map(data=pd.DataFrame({'lat':[12.521110], 'lon':[-69.968338]}), zoom=10)

        dct['location'].update({
                'coordinates': {'lat':12.521110, 'lng':-69.968338}
        })

        return dct

def property_rights():

    with st.expander('RIGHTS'):

        global keys
        dct = {'rights': {}}

        # Limitations & Access
        st.subheader('Rights and grants')
        col1, col2, col3 = st.columns([1, 1, 1])
        dct['rights'].update({
            'rights_to_land':   col1.selectbox('Rights to land', ['Freehold', 'Leasehold'], index=0, key=next(keys)),
            'right_0f_way_granted':     col2.selectbox('Right-of-way granted', ['No easement granted', 'Private easement', 'Public easement'], index=0, help=help['lot_access_granted'], key=next(keys)),
            'right_0f_way_received':    col3.selectbox('Right-of-way received', ['No easement received', 'Private easement'], index=0, help=help['lot_access_received'], key=next(keys))
        })

        st.write(' ')
        st.subheader('Zoning')
        col1, col2, col3 = st.columns([1, 1, 1])
        dct['rights'].update({
            'destination': col1.selectbox('Destination', sorted(destination), index=9, help=help['destination'], key=next(keys)),
            'designation': col2.selectbox('Designation', sorted(designation), help=help['designation'], key=next(keys))

        })

        # Spatial Development Plan
        col3.write(' ')
        col3.markdown("""<div style='text-align:center;'><a target=_blank href=https://www.arcgis.com/apps/webappviewer/index.html?id=38891684b5404974a15860c00a0defd6>Find your Zone</div>""", unsafe_allow_html=True)
        col3.write(' ')
        col3.markdown("""<div style='text-align:center;'><a target=_blank href=https://www.dip.aw/ropv/>Zoning Regulations 2021</div>""", unsafe_allow_html=True)

        # Covenants
        # st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        st.write(' ')
        st.write('**Documents**')
        dct['rights'].update({
            'documents': st.file_uploader('Upload HOA covenant', type=['pdf'], help=help['covenant'], key=next(keys))
        })

    return dct

def building(property_type):

    global keys
    dct = {key: {} for key in ['floors', 'walls', 'ceiling', 'roof', 'eds', 'images']}


    with st.expander('BUILDING'):

        lst_rooms = []
        col1, col2, col3, col4 =st.columns([1, 1, 1, 1])
        storeys = col1.number_input('Number of storeys', min_value=0, max_value=3, step=1)
        if property_type != 'Condominium':
            basement = col1.checkbox('Basement')
        else:
            basement = None

        # Basement area
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        if basement:
            # st.write(f'**{floor_trans[lvl]}**')
            col1, col2, col3, col4 = st.columns([1, 1.5, 2, 1.5])
            col1.write('**Basement**')
            dct['floors'].update({
                    'basement_area':       col2.number_input(f'Total floor area', min_value=0, step=10, key=next(keys)),
                    'basement_material':   col3.selectbox('Foundation type', options=sorted(foundation_type), key=next(keys)),
                    'basement_finish':     col4.selectbox('Floor finish', options=sorted(floor_finishes), key=next(keys)),
            })

        # Floor area
        for lvl in range(int(storeys+1)):
            # st.write(f'**{floor_trans[lvl]}**')
            col1, col2, col3, col4 = st.columns([1, 1.5, 2, 1.5])
            col1.write(f'**{floor_trans[lvl]}**')
            dct['floors'].update({
                    f"{floor_trans[lvl].lower().replace(' ', '_')}_area":       col2.number_input(f'Total floor area', min_value=0, step=10, key=next(keys)),
                    f"{floor_trans[lvl].lower().replace(' ', '_')}_material":   col3.selectbox('Foundation type', options=sorted(foundation_type), key=next(keys)),
                    f"{floor_trans[lvl].lower().replace(' ', '_')}_finish":     col4.selectbox('Floor finish', options=sorted(floor_finishes), key=next(keys)),
            })

        # Walls
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1.2, 3, 3])
        col1.write("**Walls**")
        dct['walls'].update({
                'load_bearing':    col2.selectbox('Load-bearing type', options=sorted(load_bearing), key=next(keys)),
                'partitioning':    col3.selectbox('Partitioning type', options=sorted(wall_material), key=next(keys)),
        })

        col1, col2, col3, col4 = st.columns([2.5, 3, 3, 1])
        dct['walls'].update({
                'inside_finish':   col2.selectbox('Interior finish', options=sorted(wall_finish), key=next(keys)),
                'outside_finish':  col3.selectbox('Exterior finish', options=sorted(wall_finish), key=next(keys)),
        })

        # Ceiling
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([1, 1.5, 2, 1.5])
        col1.write('**Ceiling**')
        dct['ceiling'].update({
                'height':   col2.number_input('Ceiling height (cm)', min_value=0, step=1, key=next(keys)),
                'type':     col3.selectbox('Ceiling type', options=ceiling_type, key=next(keys)),
                'material': col4.selectbox('Ceiling material', options=ceiling_material, key=next(keys)),
        })

        # Roof
        if property_type != 'Condominium':
            st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([2, 3, 1])
            col1.write('**Roof**')
            dct['roof'].update({
                'style':    col2.multiselect('Roof style(s)', options=sorted(roofs), key=next(keys)),
            })

            col1, col2, col3 = st.columns([1, 2, 2])
            dct['roof'].update({
                'roofing':  col2.selectbox('Roofing type', options=roofing.keys(), index=0, key=next(keys)),
            })

            dct['roof'].update({
                'material': col3.selectbox('Roofing material', options=roofing[dct['roof']['roofing']], key=next(keys)),
            })

            # EDS
            st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
            col1, col2 = st.columns([1, 4])
            col1.write('**Features**')
            lst_eds = col2.multiselect('Exterior domestic space', options=sorted(eds), key=next(keys))

            if lst_eds:
                columns = {f"col{index+1}": col for index, col in enumerate(st.columns([1, 1, 1, 1]))}
                for index,i in enumerate(lst_eds):
                    dct['eds'].update({
                        f'{i.lower()}': {}
                    })

                    if i == 'Patio':
                        dct['eds'][f'{i.lower()}'].update({
                            'material': columns[f"col{index+1}"].selectbox(f'{i} Material', options=sorted(eds[i]['material']), key=next(keys))
                        })

                    else:
                        dct['eds'][f'{i.lower()}'].update({
                            'style'   : columns[f"col{index+1}"].selectbox(f'{i} Style', options=sorted(eds[i]), key=next(keys))
                        })

            if dct['eds']:
                st.write(' ')
                st.write('**Images**')
                for i in dct['eds'].keys():
                    dct['images'].update({
                        f"{i}": st.file_uploader(f"Upload image of {i.replace('_', ' ').title()}", type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
                    })

    return dct

def room(num):

    global keys
    dct = {}

    st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)


    col1, col2, col3, col4 = st.columns([1, 2, 2, 2])
    col1.write(f"**ROOM {num+1}**")
    dct.update({
        'floor_area':   col2.number_input('Floor area (m2)', min_value=0, step=1, key=next(keys)),
        'room_type':    col3.selectbox('Room type', options=['Bedroom', 'Bathroom', 'Kitchen', 'Living', 'Dining', 'Laundry', 'Office', 'Other'], key=next(keys)),
        'storey':       col4.selectbox('Storey',  options=[v for v in floor_trans.values()], key=next(keys))
    })


    # Windows
    st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([1, 2.1, 2.1, 1.5])
    col1.write('**Windows**')
    dct.update({
        'window_type':          col2.multiselect('Window type', options=sorted(window_type), key=next(keys)),
        'window_frame':         col3.multiselect('Window frame material', options=sorted(frame_materials), key=next(keys)),
        'number_of_windows':    col4.number_input('Number of windows', step=1, key=next(keys)),
    })

    # Doors
    st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([1, 2.1, 2.1, 1.5])
    col1.write('**Doors**')
    dct.update({
        'door_type':        col2.multiselect('Door type', options=sorted(door_type), key=next(keys)),
        'door_material':    col3.multiselect('Door material', options=sorted(door_material), key=next(keys)),
        'number_of_doors':  col4.number_input('Number of doors', step=1, key=next(keys)),
    })

    # Features
    st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
    count = 2
    columns = {f'col{i+1}': col for i, col in enumerate(st.columns([1, 2, 2, 2]))}

    columns['col1'].write('**Features**')

    if dct['room_type'] == 'Bedroom':
        dct.update({
            'closet': columns[f'col{count}'].radio('Built-in closet', options=['Yes', 'No'], key=next(keys))
        }); count += 1


    # Bathroom
    if dct['room_type'] == 'Bathroom':
        dct.update({
            'shower': columns[f'col{count}'].number_input('Number of Shower(s)', step=1, key=next(keys))
        }); count += 1
        dct.update({
            'bathtub': columns[f'col{count}'].number_input('Number of Bathtub(s)', step=1, key=next(keys))
        }); count += 1
        dct.update({
            'wall_finish': columns[f"col{count}"].selectbox('Floor & Wall finish', options=sorted(floor_finishes), key=next(keys))
        }); count += 1


    # Kitchen
    if dct['room_type'] == 'Kitchen':
        dct.update({
            'layout': columns[f'col{count}'].multiselect('Kitchen layout', options=sorted(['One wall', 'Galley', 'L-shape', 'U-shape', 'Island', 'Peninsula']), key=next(keys))
        }); count += 1
        dct.update({
            'counter_material': columns[f'col{count}'].selectbox('Countertop material', options=countertops, key=next(keys))
        }); count += 1
        dct.update({
            'cabinet_material': columns[f'col{count}'].selectbox('Cabinet material', options=sorted(cabinet_material), key=next(keys))
        }); count += 1


    # Laundry
    if dct['room_type'] == 'Laundry':
        dct.update({
            'counter_material': columns[f'col{count}'].selectbox('Countertop material', options=countertops, key=next(keys))
        }); count += 1
        dct.update({
            'cabinet_material': columns[f'col{count}'].selectbox('Cabinet material', options=sorted(cabinet_material), key=next(keys))
        }); count += 1
        dct.update({
            'sink': columns[f'col{count}'].number_input('Sink', step=1, key=next(keys))
        }); count += 1


    # Air conditioning
    if any([dct['room_type'] == type for type in ['Bedroom', 'Living', 'Dining', 'Office', 'Other']]):
        dct.update({
            'airco': columns[f'col{count}'].radio('Air conditioning', options=['Yes', 'No'], key=next(keys))
        }); count += 1


    # Upload img
    st.write(' ')
    st.write(f"**Images**")
    dct.update({
        'images': st.file_uploader(f"Upload image of ROOM {num+1} ({dct['room_type']})", ['jpeg', 'jpg', 'png', 'gif'], key=next(keys))
    })

    return dct

def yard(lst, share_col=False):

    dct = {}
    columns = {f"col{index+1}": col  for index, col in enumerate(st.columns([1, 1, 1]))}

    for tuple in lst:

        if columns[f'col{tuple[1]}'].checkbox(f'{tuple[0].title()} yard', key=next(keys)):
            dct.update({
                f'{tuple[0]}_yard': {}
            })

            # Garden features
            dct[f'{tuple[0]}_yard'].update({
                'buildings':    columns[f'col{tuple[1]}'].multiselect('Garden building(s)', options=sorted(garden_buildings), key=next(keys)),
                'landscaping':  columns[f'col{tuple[1]}'].checkbox('Landscaping', key=next(keys)),
                'fencing':      columns[f'col{tuple[1]}'].checkbox('Fencing', key=next(keys))
            })

            # Fencing
            if dct[f'{tuple[0]}_yard']['fencing']:
                dct[f'{tuple[0]}_yard'].update({
                    'fence_ownership': columns[f'col{tuple[1]}'].radio('Fence ownership', options=['100%', '50%', '0%'], key=next(keys))
                })

    return dct

def exterior():

    global keys
    dct = {key: {} for key in ['garden', 'eds', 'adu', 'parking', 'solar', 'images']}

    with st.expander('EXTERIOR'):

        # Yard features
        st.subheader('Yards')
        dct['garden'].update(yard([('front', 2)]))
        dct['garden'].update(yard([('left', 1), ('right', 3)]))
        dct['garden'].update(yard([('back', 2)]))

        if dct['garden']:
            st.write(' ')
            st.write('**Images**')
            for i in dct['garden'].keys():
                dct['images'].update({
                    f"{i}": st.file_uploader(f"Upload image of {i.replace('_', ' ').title()}", type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
                })

        # EDS
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        st.subheader('Exterior Domestic Space')
        col1, col2, col3 = st.columns([1, 1, 1])
        lst_eds = col1.multiselect(' ', options=sorted(eds), key=next(keys))

        if lst_eds:
            for index,i in enumerate(lst_eds):
                dct['eds'].update({
                    f'{i.lower()}': {}
                })

                if index != 0:
                    col1, col2, col3 = st.columns([1, 1, 1])

                if i == 'Deck':
                    dct['eds'][f'{i.lower()}'].update({
                        'style'    : col2.selectbox(f'{i} Style', options=sorted(eds[i]['style']), key=next(keys)),
                        'matrial'  : col3.selectbox(f'{i} Material', options=sorted(eds[i]['material']), key=next(keys))
                    })

                elif i == 'Patio':
                    dct['eds'][f'{i.lower()}'].update({
                        'material': col2.selectbox(f'{i} Material', options=sorted(eds[i]['material']), key=next(keys))
                    })
                else:
                    dct['eds'][f'{i.lower()}'].update({
                        'style'   : col2.selectbox(f'{i} Style', options=sorted(eds[i]), key=next(keys))
                    })

        if dct['eds']:
            st.write(' ')
            st.write('**Images**')
            for i in dct['eds'].keys():
                dct['images'].update({
                    f"{i}": st.file_uploader(f"Upload image of {i.replace('_', ' ').title()}", type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
                })

        # ADU
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        st.subheader('Accessory Dwelling Unit')
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1.2])
        num_adu = col4.number_input('Number of ADU(s)', min_value=0, step=1, key=next(keys))

        # dct['adu'].update({'num_adu': num_adu})

        for i in range(int(num_adu)):
            st.write(f'**ADU {i+1}**')
            col1, col2, col3, col4 = st.columns([1.5, 1.5, 1.2, 1.2])

            # ADU features
            dct['adu'].update({
            f'unit_{i+1}':
                {'rental_income': col1.text_input('Last rental income (Afl.)', key=next(keys)),
                 'floor_area': col2.text_input('Floor area (m2)', key=next(keys)),
                 'num_beds': col3.number_input('Number of bedrooms', min_value=0, step=1, key=next(keys)),
                 'num_baths': col4.number_input('Number of bathrooms', min_value=0, step=1, key=next(keys))
                }
            })

        if dct['adu']:
            st.write(' ')
            st.write('**Images**')
            for i in dct['adu'].keys():
                dct['images'].update({
                    f"{i}": st.file_uploader(f"Upload image of {i.replace('_', ' ').title()}", type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
                })

        # Parking
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        st.subheader('Parking')

        col1, col2 = st.columns([2, 1])
        parkings = col1.multiselect('Type of parking space', options=parking)

        if len(parkings) > 4:
            cols = st.columns(len(parkings))
        else:
            cols = st.columns(4)

        for index, p in enumerate(parkings):
            dct['parking'].update({
                f'{p.lower()}_spaces': cols[index].number_input(f"{p} parking space(s)", min_value=0, step=1, key=next(keys))
            })

        if dct['parking']:
            st.write(' ')
            st.write('**Images**')
            for p in parkings:
                dct['parking'].update({
                    'image': st.file_uploader(f"Upload image of {p}", type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
                })

        # Solar
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        st.subheader('Solar Panels')
        col1, col2, col3 = st.columns([3, 3, 2])
        dct['solar'].update({
            'number_panels': col3.number_input('Solar panels', min_value=0, step=1, key=next(keys))
        })

        if dct['solar']['number_panels'] != 0:
            # Solar
            col1, col2, col3 =st.columns([1, 1, 1])
            dct['solar'].update({
                'solar_type':       col1.selectbox('Type of Solar panel', options=sorted(solar_type), key=next(keys)),
                'solar_capacity':   col2.number_input('Total capacity (kW)', step=1, key=next(keys)),
                'solar_savings':    col3.number_input('Savings per month (Afl.)', step=100, key=next(keys))

            })

            st.write(' ')
            st.write('**Images**')
            dct['images'].update({
                "solar_panel": st.file_uploader(f"Upload image of Solar Panels", type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
            })

        return dct

def garden():

    global keys
    dct = {key: {} for key in ['fencing', 'adu', 'parking', 'images']}

    with st.expander('GARDEN'):

        # Fencing
        col1, col2, col3, col4, col5 = st.columns([1, 3.5, 1, 1, 1])
        col1.write("**Fencing**")
        dct['fencing'].update({
            'material': col2.selectbox('Fencing material', options=fencing_material, key=next(keys)),
        })

        sides = []

        front_side = col4.checkbox('Front')
        if front_side:
            sides.append('front')
        col3.write(' ')
        col3.write(' ')
        left_side = col3.checkbox('Left')
        if front_side:
            sides.append('left')
        col5.write(' ')
        col5.write(' ')
        right_side = col5.checkbox('Right')
        if front_side:
            sides.append('right')
        col4.write(' ')
        col4.write(' ')
        back_side = col4.checkbox('Back')
        if front_side:
            sides.append('back')

        dct['fencing'].update({'sides': sides})

        # Outdoor flooring
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 6.5])
        col1.write("**Flooring**")
        dct.update({
            'outdoor_flooring': col2.multiselect('Outdoor flooring', options=outdoor_flooring, key=next(keys))
        })

        # Garden buildings
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 4.5, 1.5])
        col1.write("**Building**")
        dct.update({
            'garden_buildings': col2.multiselect('Garden buildings', options=garden_buildings, key=next(keys))
        })

        # ADU
        num_adu = col3.number_input('Number of ADU(s)', min_value=0, step=1, key=next(keys), help=help['adu'])
        for i in range(int(num_adu)):
            col1, col2, col3, col4, col5 = st.columns([1, 1.5, 1.5, 1.5, 1.5])
            col1.write(f'**ADU {i+1}**')
            # ADU features
            dct['adu'].update({
            f'unit_{i+1}':
                {'rental_income': col2.text_input('Rental income (Afl.)', key=next(keys)),
                 'floor_area': col3.text_input('Floor area (m2)', key=next(keys)),
                 'bedrooms': col4.number_input('Bedrooms', key=next(keys)),
                 'bathrooms': col5.number_input('Bathrooms', key=next(keys))
                }
            })


        # Parking
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 4.5, 1.5])
        col1.write('**Parking**')
        dct['parking'].update({
            'parking_types': col2.multiselect('Parking space', options=parking),
            'parking_spaces': col3.number_input("Total parking space(s)", min_value=0, step=1, key=next(keys))
        })

        # images
        st.write(' ')
        st.write('**Images**')
        col1, col2 = st.columns([1, 1])
        dct['images'].update({
            'front_yard': col1.file_uploader(f"Upload image of front yard", type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
            'right_yard': col1.file_uploader(f"Upload image of right yard", type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
            'back_yard': col2.file_uploader(f"Upload image of backyard", type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
            'left_yard': col2.file_uploader(f"Upload image of left yard", type=['png', 'jpg', 'jpeg', 'gif'], key=next(keys)),
        })

        return dct

def amenities():

    global keys
    dct = {}

    with st.expander('AMENITIES'):

        col1, col2= st.columns([1, 4])
        col1.write('**Distinctive**')
        dct.update({
            'idistinctive_features':    col2.multiselect('Distinctive features', options=sorted(distinctive_features), key=next(keys)),
        })

        col1, col2 = st.columns([1, 4])
        col1.write('**Recreation**')
        dct.update({
            'recreation': col2.multiselect('Select recreational areas', options=sorted(recreation), key=next(keys))
        })

        col1, col2 = st.columns([1, 4])
        col1.write('**Pets**')
        dct.update({
            'pet': col2.multiselect('Pet amenities', options=sorted(pet_amenities), key=next(keys)),
        })
        col1, col2 = st.columns([1, 4])
        col1.write('**Parking**')
        dct.update({
            'parking': col2.multiselect('Parking amenities', options=sorted(parking_amenities), key=next(keys)),
        })

        col1, col2 = st.columns([1, 4])
        col1.write('**Community**')
        dct.update({
            'community_amenities':  col2.multiselect('Community amentities', options=sorted(community_amenities), key=next(keys)),
        })

        col1, col2= st.columns([1, 4])
        col1.write('**In-unit**')
        dct.update({
            'in_unit_amenities':    col2.multiselect('In-unit amenities', options=sorted(in_unit_amenities), key=next(keys)),
        })

    return dct

def appraisal(type='Land'):

    with st.expander('APPRAISAL'):

        global keys
        dct = {'appraisal': {}}

        # Contact info
        st.write(' ')
        st.subheader('Appraisor contact info')
        col1, col2, col3 = st.columns([1, 1, 1])
        dct['appraisal'].update({
            'company_name': col1.text_input('Company name', key=next(keys))
        })

        dct['appraisal'].update({
            'first_name': col2.text_input('First name', key=next(keys)),
            'last_name': col3.text_input('Last name', key=next(keys))
        })

        col1, col2 = st.columns([1, 2])
        dct['appraisal'].update({
            'company phone': col1.text_input('Company phone', key=next(keys))
            })
        dct['appraisal'].update({
            'email_address': col2.text_input('Email address', key=next(keys))
            })

        # Appraisal
        st.write(' ')
        st.write('**Appraisal values**')
        col1, col2, col3 = st.columns([1, 1, 1])
        dct['appraisal'].update({
            'market_value': col1.text_input('Market value (Afl.)', key=next(keys)),
            'execution_value': col2.text_input('Foreclosure value (Afl.)', key=next(keys), help=help['foreclosure'])
        })

        if type != 'Land':
            dct['appraisal'].update({
                'reconstruction_value': col3.text_input('Reconstruction (Afl.)', key=next(keys))
            })
        else:
            dct['appraisal'].update({
                'reconstruction_value': col3.text_input('Reconstruction (Afl.)', key=next(keys))
            })

        # Upload
        st.write(' ')
        st.write('**Documents**')
        dct['appraisal'].update({
            'documents': st.file_uploader('Upload Appraisal Report', type=['pdf'], key=next(keys))
        })

        return dct

def financials():

    with st.expander('OBLIGATIONS'):

        global keys
        dct = {'obligations': {'liens': {}, 'taxes': {}}}

        # Liens
        st.subheader('Liens')
        col1, col2 = st.columns([1, 1])
        dct['obligations']['liens'].update({
            'type_of_lien': col1.selectbox('Type of Lien', ['None', 'Consensual', 'Statutory', 'Judgement'], help=help['liens'], key=next(keys)),
            'open_balance': col2.text_input('Open balance (Afl.)', key=next(keys))
        })

        # Contact INFO
        st.write(' ')
        st.subheader("Contact info")
        col1, col2, col3 = st.columns([1, 1, 1])
        dct['obligations']['liens'].update({
            'company_name': col1.text_input('Institution / Company name'),
            'first_name':   col2.text_input('First name'),
            'last_name':    col3.text_input('Last name'),
        })

        col1, col2 = st.columns([1, 2])
        dct['obligations']['liens'].update({
            'phone_number': col1.text_input('Phone number'),
            'email':        col2.text_input('Email address')
        })

        # Upload Certificate of Title
        st.write(' ')
        st.write('**Documents**')
        dct['obligations']['liens'].update({
            'documents': st.file_uploader('Upload Certificate of Title', type=['pdf'], help=help['title'])
        })


        # Taxes
        st.markdown("""<hr style='border: none;height: 1px;background:linear-gradient(to right, white, red, white);'>""", unsafe_allow_html=True)
        st.subheader('Taxes')
        col1, col2, col3 = st.columns([1, 1, 1])
        dct['obligations']['taxes'].update({
            'register_value': col1.text_input('Register value (Afl.)', help=help['register_value']),
            'land_tax': col2.text_input('Land tax (Afl.)', help=help['land_tax'])
        })


        # Ground lease & Canon obligation
        st.write('**Documents**')
        dct['obligations']['taxes'].update({
            'documents': {
                'register_value': st.file_uploader('Upload register value document', type=['pdf']),
                'land_tax': st.file_uploader('Upload land tax document', type=['pdf'])
            }
        })


    return dct


if __name__ == '__main__':

    # Style radio button horizontally
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)

    keys = iter(range(999))
    current_year = datetime.datetime.today().year

    property_type = st.sidebar.selectbox('Property type', options=['Land', 'House', 'Apartment', 'Condominium', 'Commercial'])

    dct = general_info(property_type)

    dct.update(location())

    dct.update(property_rights())

    if property_type != 'Land':

        dct.update({
            'building': building(property_type)
        })

        with st.expander('ROOMS'):
            col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
            num = col1.number_input('Number of rooms', min_value=0, step=1)
            dct.update({
                'interior': [room(i) for i in range(int(num))]
            })

        if property_type == 'Condominium' or property_type == 'Apartment':

            dct.update({
                'amenities': amenities()
            })
        else:
            dct.update({
                'garden': garden()
            })

    dct.update(appraisal(property_type))

    dct.update(financials())

    st.write(dct)

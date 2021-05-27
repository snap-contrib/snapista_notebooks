import os

from pystac import Item, Catalog, CatalogType, extensions
from urllib.parse import urlparse

def test(txt):
    print(txt)
    
def get_items(catalog):

    cat = Catalog.from_file(catalog) 

    items = []

    for item in iter(cat.get_items()):

        items.append(item)
    
    return items


def get_item(catalog):
    
    cat = Catalog.from_file(catalog) 

    try:
        
        collection = next(cat.get_children())
        
        item = next(collection.get_items())        
        
    except StopIteration:
        
        item = next(cat.get_items())
        
    return item

def get_bands(item):
    
    eo_item = extensions.eo.EOItemExt(item)
    
    return [b.common_name for b in eo_item.bands]

def get_asset(item, band_name):
    
    asset = None
    
    eo_item = extensions.eo.EOItemExt(item)
    
    # Get bands
    if (eo_item.bands) is not None:
  
        for index, band in enumerate(eo_item.bands):
            
            print(item.assets)
            print(item.assets.keys())
            
            if band.name in item.assets.keys():
                
                asset = item.assets[band.name]
                print(asset)
                asset.href = fix_asset_href(asset.get_absolute_href())
                print(asset.href)
                
                stop
                
                
#             print(index, band.name, band.common_name)
#             print(item.assets)
            
#             stop
            
#             if band.common_name in [band_name]: 
#                 asset = item.assets[band.name]
#                 print(asset)
#                 stop
#                 try:
#                     asset = item.assets[band.common_name] # for L2A products (not calibrated for charter)
#                     asset.href = fix_asset_href(asset.get_absolute_href())
                    
#                     print(index, band.name, band.common_name, asset.href)
            
#                 except:
#                     print(f'{index}, {band.name}, {band.common_name} --> no assets')
                    
# #                 
#                 break
    
    return asset

def get_item_property(item, prop):

    if prop in item.properties.keys():

        return item.properties[prop]

    else:

        return None


def get_asset_property(item, band_name, prop):

    for asset_key in item.get_assets():

        asset = item.get_assets()[asset_key]

        if 'eo:bands' in asset.properties.keys():

            for index, band in enumerate(asset.properties['eo:bands']):

                if band['common_name'] == band_name:

                    if prop in asset.properties["eo:bands"][index].keys():

                        return asset.properties["eo:bands"][index][prop]

def fix_asset_href(uri):
    print('-', uri)
    parsed = urlparse(uri)
    
    if parsed.scheme.startswith('http'):
        
        return '/vsicurl/{}'.format(uri)
    
    elif parsed.scheme.startswith('file'):

        return uri.replace('file://', '')

    else:
        
        return uri
    

def has_pan(item):
    
    if get_asset(item, 'pan'):
        return True
    else:
        return False
    

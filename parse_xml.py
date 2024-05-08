import xml.etree.ElementTree as ET
import pandas as pd

xml_data = '''
<products>
    <product>
        <id>1</id>
        <name>Laptop</name>
        <category>Electronics</category>
        <price>800</price>
    </product>
    <!-- Add more product entries here -->
</products>
'''

root = ET.fromstring(xml_data)

product_data = []
for product in root.findall('product'):
    product_dict = {
        'ID': product.find('id').text,
        'Name': product.find('name').text,
        'Category': product.find('category').text,
        'Price': float(product.find('price').text)
    }
    product_data.append(product_dict)

# Create a DataFrame from the parsed data
df = pd.DataFrame(product_data)

# Save the DataFrame to a CSV file
df.to_csv('product_data.csv', index=False)

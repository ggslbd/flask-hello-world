import pandas as pd

def find_tag_description(tag_name):
    
    csv_file_path = "web-config.csv"
    
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Find the tag_description for the specified tag_name
        result = df[df['tag_name'] == tag_name]
        
        # Check if a result was found
        if not result.empty:
            tag_description = result.iloc[0]['tag_description']
            return tag_description
        else:
            return f"No tag found with the name '{tag_name}'"
    except FileNotFoundError:
        return f"File not found: {csv_file_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"



# Ask the user for the tag_name they want to look up
tag_name_to_find = input("Enter the tag_name you want to find: ")

# Call the function to find the tag_description
result = find_tag_description(tag_name_to_find)

# Print the result
print(result)




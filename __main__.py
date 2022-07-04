import src.input_window as input_window

week_dict = {'This Week': 0, 'Next Week': 1, 'Two Weeks From Now':2 }
index_url = 'https://www.toronto.ca/data/parks/live/locations/centres.json?_=1655614708813'

def main():
    input_window.create(index_url, week_dict)

if __name__ == "__main__":
    main()
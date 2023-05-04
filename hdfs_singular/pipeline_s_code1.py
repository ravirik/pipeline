import argparse
import requests
from hdfs import InsecureClient

def retrieve_data(api_url, api_params):
        response = requests.get(api_url, params=api_params)
            data = response.json()
                return data

            def store_data_hdfs(data, hdfs_url, hdfs_path):
                    client = InsecureClient(hdfs_url)
                        with client.write(hdfs_path, encoding="utf-8") as writer:
                                    writer.write(str(data))

                                    if __name__ == "__main__":
                                            parser = argparse.ArgumentParser(description="Retrieve data from a web API and store it in HDFS.")
                                                parser.add_argument("api_url", help="URL of the web API.")
                                                    parser.add_argument("api_param1", help="First parameter for the API request.")
                                                        parser.add_argument("api_param2", help="Second parameter for the API request.")
                                                            parser.add_argument("hdfs_url", help="URL of the HDFS cluster.")
                                                                parser.add_argument("hdfs_path", help="HDFS path to store the data.")
                                                                    args = parser.parse_args()

                                                                        api_url = args.api_url
                                                                            api_params = {"param1": args.api_param1, "param2": args.api_param2}
                                                                                hdfs_url = args.hdfs_url
                                                                                    hdfs_path = args.hdfs_path

                                                                                        data = retrieve_data(api_url, api_params)
                                                                                            store_data_hdfs(data, hdfs_url, hdfs_path)


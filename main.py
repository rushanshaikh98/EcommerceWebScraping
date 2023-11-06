"""This file is for running the app"""

from core import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)



# try:
        #     url = input_json["url"]
        #     domain_name = urllib.parse.urlparse(url).hostname
        #     if domain_name in urls_and_function:
        #         data = subprocess.run(['scrapy', 'crawl', urls_and_function[domain_name], "-a", f'product_url={url}'], capture_output=True, text=True)
        #         return eval(data.stdout)
        #     else:
        #         return {"data": [], "message": "Please enter valid url",
        #                 "status": "FALSE"}, status.HTTP_400_BAD_REQUEST
        # except (KeyError, AttributeError):
        #     return {"data": [], "message": "No proper data", "status": "FALSE"}, status.HTTP_400_BAD_REQUEST
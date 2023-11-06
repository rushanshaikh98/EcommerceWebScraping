from flask import Blueprint

from core.api.services import ProductDetailAPI

api_routes = Blueprint("scrappers", __name__)

api_routes.add_url_rule("/api/get/product_details", view_func=ProductDetailAPI.as_view("get_product_details"))

from django.urls import path
from django.views.generic import TemplateView
urlpatterns = [
    path('about/', TemplateView.as_view(template_name="about.html" ), name="about"),
	path('blog_2/', TemplateView.as_view(template_name="blog-2.html" ), name="blog_2"),
	path('blog_detail/', TemplateView.as_view(template_name="blog-detail.html" ), name="blog_detail"),
	path('blog/', TemplateView.as_view(template_name="blog.html" ), name="blog"),
	path('cart_page/', TemplateView.as_view(template_name="cart-page.html" ), name="cart_page"),
	path('checkout/', TemplateView.as_view(template_name="checkout.html" ), name="checkout"),
	path('commercial_interior/', TemplateView.as_view(template_name="commercial-interior.html" ), name="commercial_interior"),
	path('contact/', TemplateView.as_view(template_name="contact.html" ), name="contact"),
	path('false_celling_design/', TemplateView.as_view(template_name="false-celling-design.html" ), name="false_celling_design"),
	path('hospitality_design/', TemplateView.as_view(template_name="hospitality-design.html" ), name="hospitality_design"),
	path('index_2/', TemplateView.as_view(template_name="index-2.html" ), name="index_2"),
	path('index_3/', TemplateView.as_view(template_name="index-3.html" ), name="index_3"),
	path('index_4/', TemplateView.as_view(template_name="index-4.html" ), name="index_4"),
	path('index_5/', TemplateView.as_view(template_name="index-5.html" ), name="index_5"),
	path('index_6/', TemplateView.as_view(template_name="index-6.html" ), name="index_6"),
	path('', TemplateView.as_view(template_name="index.html" ), name="index"),
	path('modern_furniture/', TemplateView.as_view(template_name="modern-furniture.html" ), name="modern_furniture"),
	path('modular_kitchen/', TemplateView.as_view(template_name="modular-kitchen.html" ), name="modular_kitchen"),
	path('office_interior/', TemplateView.as_view(template_name="office-interior.html" ), name="office_interior"),
	path('product_detail/', TemplateView.as_view(template_name="product-detail.html" ), name="product_detail"),
	path('projects_classic/', TemplateView.as_view(template_name="projects-classic.html" ), name="projects_classic"),
	path('projects_fullwidth/', TemplateView.as_view(template_name="projects-fullwidth.html" ), name="projects_fullwidth"),
	path('projects_masonry/', TemplateView.as_view(template_name="projects-masonry.html" ), name="projects_masonry"),
	path('residental_interior/', TemplateView.as_view(template_name="residental-interior.html" ), name="residental_interior"),
	path('services_dark/', TemplateView.as_view(template_name="services-dark.html" ), name="services_dark"),
	path('services_light/', TemplateView.as_view(template_name="services-light.html" ), name="services_light"),
	path('shop/', TemplateView.as_view(template_name="shop.html" ), name="shop"),
	path('team/', TemplateView.as_view(template_name="team.html" ), name="team"),
	path('testimonials/', TemplateView.as_view(template_name="testimonials.html" ), name="testimonials"),
	path('wardrobe/', TemplateView.as_view(template_name="wardrobe.html" ), name="wardrobe"),

]

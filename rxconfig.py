import reflex as rx

config = rx.Config(
    app_name="por_siempre_raul_y_tatiana",
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.sitemap.SitemapPlugin,
        rx.plugins.RadixThemesPlugin
    ],
)
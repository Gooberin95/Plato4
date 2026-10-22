import reflex as rx

config = rx.Config(
    app_name="copper_latitude",
    telemetry_enabled=False,
    frontend_port=3000,
    backend_port=8000,
    disable_plugins=[rx.plugins.SitemapPlugin],
    plugins=[
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="amber",
                gray_color="sand",
                radius="none",
                has_background=False,
            )
        )
    ],
)

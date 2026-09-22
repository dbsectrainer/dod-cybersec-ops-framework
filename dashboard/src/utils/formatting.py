"""
UI Formatting Utilities

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""


def format_classification_banner():
    """Return formatted classification banner HTML."""
    return """
    <div style='background-color: #f0f2f6; padding: 10px; text-align: center; font-weight: bold;'>
        UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
    </div>
    """


def format_footer():
    """Return formatted footer HTML."""
    return """
    <div style='background-color: #f0f2f6; padding: 10px; text-align: center;'>
        <small>DoD Cybersecurity Operations Framework - For Official Use Only</small>
    </div>
    """


def format_metric_container(title, metrics, style="default"):
    """Format a metric container with consistent styling.

    Args:
        title (str): Container title
        metrics (dict): Dictionary of metrics to display
        style (str): Style variant ('default', 'warning', 'success', 'info')
    """
    styles = {
        "default": {"bg_color": "#f8f9fa", "border_color": "#dee2e6", "text_color": "#212529"},
        "warning": {"bg_color": "#fff3cd", "border_color": "#ffeeba", "text_color": "#856404"},
        "success": {"bg_color": "#d4edda", "border_color": "#c3e6cb", "text_color": "#155724"},
        "info": {"bg_color": "#d1ecf1", "border_color": "#bee5eb", "text_color": "#0c5460"},
    }

    style_config = styles.get(style, styles["default"])

    html = f"""
    <div style='
        background-color: {style_config["bg_color"]};
        border: 1px solid {style_config["border_color"]};
        color: {style_config["text_color"]};
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    '>
        <h4 style='margin-top: 0;'>{title}</h4>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px;'>
    """

    for key, value in metrics.items():
        html += f"""
            <div style='padding: 10px; background-color: rgba(255,255,255,0.5); border-radius: 3px;'>
                <div style='font-size: 0.9em; color: {style_config["text_color"]};'>
                    {key.replace("_", " ").title()}
                </div>
                <div style='font-size: 1.2em; font-weight: bold;'>
                    {value}
                </div>
            </div>
        """

    html += """
        </div>
    </div>
    """

    return html


def format_alert(message, level="info"):
    """Format an alert message with consistent styling.

    Args:
        message (str): Alert message
        level (str): Alert level ('info', 'success', 'warning', 'error')
    """
    styles = {
        "info": {
            "bg_color": "#cce5ff",
            "border_color": "#b8daff",
            "text_color": "#004085",
            "icon": "ℹ️",
        },
        "success": {
            "bg_color": "#d4edda",
            "border_color": "#c3e6cb",
            "text_color": "#155724",
            "icon": "✅",
        },
        "warning": {
            "bg_color": "#fff3cd",
            "border_color": "#ffeeba",
            "text_color": "#856404",
            "icon": "⚠️",
        },
        "error": {
            "bg_color": "#f8d7da",
            "border_color": "#f5c6cb",
            "text_color": "#721c24",
            "icon": "❌",
        },
    }

    style = styles.get(level, styles["info"])

    return f"""
    <div style='
        background-color: {style["bg_color"]};
        border: 1px solid {style["border_color"]};
        color: {style["text_color"]};
        padding: 12px;
        border-radius: 4px;
        margin: 10px 0;
        display: flex;
        align-items: center;
    '>
        <span style='margin-right: 10px;'>{style["icon"]}</span>
        {message}
    </div>
    """


def format_table(data, headers=None, style="default"):
    """Format a table with consistent styling.

    Args:
        data (list): List of dictionaries containing row data
        headers (list): Optional list of column headers
        style (str): Table style variant ('default', 'compact', 'striped')
    """
    styles = {
        "default": {
            "border_color": "#dee2e6",
            "header_bg": "#f8f9fa",
            "row_bg": "#ffffff",
            "alt_row_bg": "#ffffff",
        },
        "compact": {
            "border_color": "#dee2e6",
            "header_bg": "#e9ecef",
            "row_bg": "#ffffff",
            "alt_row_bg": "#ffffff",
        },
        "striped": {
            "border_color": "#dee2e6",
            "header_bg": "#f8f9fa",
            "row_bg": "#ffffff",
            "alt_row_bg": "#f8f9fa",
        },
    }

    style_config = styles.get(style, styles["default"])

    html = f"""
    <div style='
        border: 1px solid {style_config["border_color"]};
        border-radius: 4px;
        overflow: hidden;
    '>
        <table style='width: 100%; border-collapse: collapse;'>
    """

    if headers:
        html += "<thead>"
        html += f"<tr style='background-color: {style_config['header_bg']};'>"
        for header in headers:
            html += f"""
                <th style='
                    padding: 12px;
                    border-bottom: 2px solid {style_config["border_color"]};
                    text-align: left;
                    font-weight: bold;
                '>
                    {header}
                </th>
            """
        html += "</tr></thead>"

    html += "<tbody>"
    for i, row in enumerate(data):
        bg_color = style_config["alt_row_bg"] if i % 2 else style_config["row_bg"]
        html += f"<tr style='background-color: {bg_color};'>"
        for value in row.values():
            html += f"""
                <td style='
                    padding: 12px;
                    border-top: 1px solid {style_config["border_color"]};
                '>
                    {value}
                </td>
            """
        html += "</tr>"
    html += "</tbody></table></div>"

    return html

import traceback

def check_runtime(code):

    try:
        exec(code, {})
        return {
            "success": True,
            "message": "No runtime errors"
        }

    except Exception as e:

        return {
            "success": False,
            "error_type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc()
        }
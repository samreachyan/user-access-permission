MESSAGES = {
    "en": {
        "user_created": "User created successfully.",
        "login_success": "Login successful.",
        "unauthorized": "Unauthorized.",
        "forbidden": "Forbidden.",
        "not_found": "Resource not found.",
        "bad_request": "Bad request.",
        "internal_error": "Internal server error."
    },
    "km": {
        "user_created": "បានបង្កើតអ្នកប្រើប្រាស់ដោយជោគជ័យ។",
        "login_success": "ការចូលប្រើបានជោគជ័យ។",
        "unauthorized": "មិនមានសិទ្ធិ។",
        "forbidden": "ហាមឃាត់។",
        "not_found": "រកមិនឃើញធនធាន។",
        "bad_request": "សំណើមិនត្រឹមត្រូវ។",
        "internal_error": "បញ្ហាក្នុងម៉ាស៊ីនមេ។"
    },
    "vn": {
        "user_created": "Tạo người dùng thành công.",
        "login_success": "Đăng nhập thành công.",
        "unauthorized": "Không được phép.",
        "forbidden": "Bị cấm.",
        "not_found": "Không tìm thấy tài nguyên.",
        "bad_request": "Yêu cầu không hợp lệ.",
        "internal_error": "Lỗi máy chủ nội bộ."
    }
}

def get_message(key: str, lang: str = "en"):
    return MESSAGES.get(lang, MESSAGES["en"]).get(key, key)

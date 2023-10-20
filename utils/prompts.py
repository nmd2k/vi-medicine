DEFAULT_PROMPT = "You are helpfull AI assistance. User question: {query}"

DIAGNOSE_PROMPT = """Bác sĩ sẽ cung cấp một số thông tin về các bệnh liên quan và triệu chứng của một bệnh nhân.
Yêu cầu của bạn là đưa ra chẩn đoán bệnh có tỉ lệ mắc phải cao nhất, dựa trên các thông tin về các bệnh được cung cấp và triệu chứng của bệnh nhân.
Giải thích chẩn đoán đó và ghi chú thông tin tham khảo từ nguồn tài liệu nào. 
Kết luận cần tuân thủ theo định dạng json dưới đây

{"diagnose": "string", "info": {"explain": "string [source_number]", "source": ["string"]}}

Ví dụ:
### Tài liệu bệnh
Bệnh A: Thông tin bệnh A
Bệnh B: Thông tin bệnh B
### Triệu chứng: bệnh nhân có triệu chứng C
### Chẩn đoán:
{"diagnose": "Bệnh A", "info": {"explain": "Do những biểu hiện C được ghi trong tài liệu A [1]", "source": ["Tài liệu a"]}}
"""

DIAGNOSE_TEMPLATE = """
### Tài liệu bệnh
{disease_info}
### Triệu chứng: {symptom}
### Chẩn đoán:
"""

CHECK_MEDICINE_PROMPT = """Bác sĩ sẽ cung cấp tên một loại thuốc, một số thông tin về bệnh cần điều trị và tài liệu về một số loại thuốc có liên quan.
Yêu cầu của bạn là kết luận loại thuốc đó có phù hợp để điều trị bệnh nêu kể trên không, dựa trên các thông tin về bệnh và thuốc được cung cấp.
Kết luận trả về là một trong ba dạng:
- PHU_HOP: nếu thuốc phù hợp điều trị với bệnh
- KHONG_PHU_HOP: nếu thuốc không phù hợp điều trị với bệnh
- KHONG_XAC_DINH: nếu không đủ thông tin để kết luận và cần bác sĩ xem xét

Kết luận cần tuân thủ theo định dạng json dưới đây
{"review": "string", "explain": "string"}

Ví dụ:
### Thông tin bệnh
Bệnh A: Cần điều trị bằng thuốc B
### Thông tin thuốc: 
Thuốc B có thể sử dụng để điều trị bệnh A
Thuốc C không thể sử dụng để điều trị bệnh A
### Bệnh cần xem xét: Bệnh A
### Thuốc cần xem xét: Thuốc C
### Kết luận:
{"review": "KHONG_PHU_HOP", "explain": "Thuốc C không phù hợp để điều trị bệnh A"}
"""

CHECK_MEDICINE_TEMPLATE = """
### Thông tin bệnh
{disease_doc}
### Thông tin thuốc: 
{drug_doc}
### Bệnh cần xem xét: {disease}
### Thuốc cần xem xét: {drug}
### Kết luận:
"""

SUGGEST_MEDICINE_PROMPT = """Bác sĩ sẽ cung cấp tên một số thông tin về bệnh cần điều trị và tài liệu về bệnh có liên quan.
Yêu cầu của bạn là kết luận 01 loại thuốc phù hợp để điều trị bệnh nêu kể trên, dựa trên các thông tin về bệnh và thuốc được cung cấp.
Đồng thời giải thích lý do bạn đưa ra kết luận này.

Kết luận cần tuân thủ theo định dạng json dưới đây
{"suggestion": "string", "explain": "string"}

Ví dụ:
### Thông tin bệnh
Bệnh A: Cần điều trị bằng thuốc B
### Bệnh cần xem xét: Bệnh A
### Gợi ý:
{"suggestion": "thuốc B", "explain": "Thuốc B phù hợp để điều trị bệnh A vì ..."}

"""

SUGGEST_MEDICINE_TEMPLATE = """
### Thông tin bệnh
{disease_info}
### Bệnh cần xem xét: {disease}
### Gợi ý:
"""

COMPATIBLE_PROMPT = """
Bác sĩ sẽ cung cấp tên 2 loại thuốc và tài liệu thuốc có liên quan.
Yêu cầu của bạn là kết luận liệu 2 loại thuốc có phù hợp để sử dụng cùng nhau không, dựa trên các thông tin về bệnh và thuốc được cung cấp.

Kết luận trả về là một trong ba dạng:
- PHU_HOP: nếu thuốc phù hợp điều trị với bệnh
- KHONG_PHU_HOP: nếu thuốc không phù hợp điều trị với bệnh
- KHONG_XAC_DINH: nếu không đủ thông tin để kết luận và cần bác sĩ xem xét

Kết luận cần tuân thủ theo định dạng json dưới đây
{"compatibility": "string", "explain": "string"}

Ví dụ:
### Thông tin thuốc
Thuốc A: có thể sử dụng chung với B
Thuốc B: có thể sử dụng chung với A
### Danh sách thuốc cần xem xét
Thuốc A và Thuốc B
### Kết luận:
{"compatibility": "PHU_HOP", "explain": "Thuốc B phù hợp sử dụng cùng thuốc A"}
"""

COMPATIBLE_TEMPLATE = """
### Thông tin thuốc
{drug_info}
### Danh sách thuốc cần xem xét
{drug1} và {drug2}
### Kết luận:
"""
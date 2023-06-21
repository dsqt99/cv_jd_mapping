ROOT_DATADIR = 'data'
stop_words_path = 'utils/vietnamese-stopwords-dash.txt'

cs_threshold = 0.7

feature_weights = {
    'gender': 0.05,
    'working_form': 0.05,
    'rank': 0.05,
    'main_career': 0.07,
    'sub_career': 0.03,
    'work_province': 0.1,
    'work_district': 0.01,
    'level_learning': 0.05,
    'certificate': 0.05,
    'work_experience': 0.15,
    'title': 0.05,
    'skill': 0.01,
    'job_description': 0.1,
    'job_requirement': 0.1,
    'job_benefit': 0.04,
    'salary': 0.09
}

capbac = {
    0: "Cấp bậc mong muốn",
    1: "Mới tốt nghiệp",
    2: "Thực tập sinh",
    3: "Nhân viên",
    4: "Trưởng phòng",
    5: "Phó giám đốc",
    6: "Giám đốc",
    7: "Tổng giám đốc điều hành",
}

hinhthuc = {
    0: "Hình thức làm việc",
    1: "Toàn thời gian cố định",
    2: "Toàn thời gian tạm thời",
    3: "Bán thời gian",
    4: "Bán thời gian tạm thời",
    5: "Hợp đồng",
    6: "Khác",
}

hocvan = {
    0: "Trình độ học vấn",
    1: "Không yêu cầu",
    5: "Trung học",
    4: "Cao đẳng",
    3: "Đại học",
    2: "Sau đại học",
    6: "Cử nhân",
    8: "Thạc sĩ",
    9: "Thạc sĩ Nghệ thuật",
    10: "Thạc sĩ Thương mại",
    11: "Thạc sĩ Khoa học",
    12: "Thạc sĩ Kiến trúc",
    13: "Thạc sĩ QTKD",
    14: "Thạc sĩ Kỹ thuật ứng dụng",
    15: "Thạc sĩ Luật",
    16: "Thạc sĩ Y học",
    17: "Thạc sĩ Dược phẩm",
    18: "Tiến sĩ",
    19: "Khác",
}

exp = {
    0: "Chưa có kinh nghiệm",
    1: "dưới 1 năm",
    2: "1 năm",
    3: "2 năm",
    4: "3 năm",
    5: "4 năm",
    6: "5 năm",
    7: "5 - 10 năm",
    8: "trên 10 năm",
    9: "trên 20 năm",
}

sex = {
    0: "Giới tính",
    1: "Nam",
    2: "Nữ",
    3: 'Khác'
}

salary = {
    0: "Mức lương",
    1: "Thỏa thuận",
    2: "Từ 3 - 5 triệu",
    3: "Từ 6 - 8 triệu",
    4: "Từ 9 - 10 triệu",
    5: "Từ 11 - 12 triệu",
    6: "Từ 13 - 15 triệu",
    7: "Từ 16 - 20 triệu",
    8: "Từ 21 - 25 triệu",
    9: "Từ 26 - 30 triệu",
    10: "Từ 31 - 40 triệu",
    11: "Từ 41 - 50 triệu",
    12: "Từ 51 - 60 triệu",
    13: "Trên 60 triệu",
}

capnhat = {
    0: "Thời gian",
    1: "Hôm nay",
    2: "Tuần này",
    3: "Tháng này",
}

trangthai_uv = {
    0: "Tất cả trạng thái hồ sơ",
    1: "CV tiếp nhận",
    2: "Phù hợp",
    3: "Hẹn phỏng vấn",
    4: "Gửi đề nghị",
    5: "Nhận việc",
    6: "Từ chối"
}
nguon_hs = {
    0: "Tất cả nguồn hồ sơ",
    1: "Ứng tuyển",
    2: "Job3s hỗ trợ",
    3: "Hồ sơ đã lưu",
    4: "Hồ sơ từ điểm lọc",
}
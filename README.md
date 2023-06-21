# Resume and job description matching Algorithm
- Job description là đoạn văn bản được lấy từ “Mô tả công việc” (gồm các ý được nhà tuyển dụng soạn ra).

- Resume được lấy từ CV ứng viên gửi lên.

- Quá trình đánh giá độ tương đồng là:

    + Do mô tả công việc được nhà tuyển dụng soạn thành các ý gạch đầu dòng ngẫu nhiên về yêu cầu nên thuật toán sẽ tính độ tương đồng cosine similarity của từng câu trong mô tả công việc với từng đặc tính của CV.

	+ Với mỗi câu, nếu độ tương đồng với tất cả các đặc tính của CV nhỏ hơn ngưỡng threshold thì ta lấy trung bình tất cả các tương đồng của các đặc tính làm độ tương đồng câu mô tả công việc đó với CV.

	+ Với câu mô tả công việc có độ tương đồng với một vài đặc tính CV > threshold thì ta lấy trung bình các độ tương đồng lớn hơn threshold làm độ tương đồng câu mô tả công việc đó với CV.

# Test on local
## Create virtual environment (optional)
```
conda create -n cv_matcher python=3.9
conda activate cv_matcher
```

## Install requirements
```
pip install -r requirements.txt
```

## Run test to see the result in file result.json
```
sh test.sh
```

# Run API 

## On Server DEV 158.247.192.219

Install requirements
```
pip3.9 install -r requirements.txt
```

Run
```
python3.9 app.py
```

## Run with Docker
```
docker build -t cv_matcher .
docker run -p 2312:2312 --network=host cv_matcher:latest
```
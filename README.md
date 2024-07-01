> # CycleGAN Augmentation

- 주제: CycleGAN을 이용한 데이터 증강과 이를 통한 자동 분류 시스템 개선
- 부제: YOLO를 이용한 자동 분류 시스템
- from Recyclear (AIC)
- 작성에 기여한 부분이 있는 코드 모음
- 2021.12.30 ~

---

- 추가 data 수집
- 낮 data -> 밤 data 변환 (실내외 image 차이, 분류기 학습용 생성 data와 crawling data 차이)
- CycleGAN: original, ResNet(야간 데이터 변환 관련 논문 참고,) SRGAN(해상도 개선)
  - loss: Perceptual loss(Adversarial + Content), Cycle-consistency loss, Identity loss

<!-- 이전에 교수님께서 말씀하셨던 것처럼 추가 학습이 필요한 클래스가 아니라 전체 데이터에 대한 학습을 진행할 것.
그리고 데이터를 빠르게 만들어서 학습을 진행할 것.
처음 그림이 상당히 잘 나왔다. 계속 잘 나왔으면 좋겠다. -->

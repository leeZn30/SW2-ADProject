while True:
    if self.user_sum == self.dealer_sum:
        self.dealerFinished()
        break
    elif self.dealer_sum > 21:
        self.dealerFinished()
        break
    elif self.dealer_sum == 21:
        self.dealerFinished()
        break
    elif self.dealer_to_21 < self.user_to_21:
        self.dealerFinished()
        break

    d_lbl = QLabel(self)
    d_card = random.sample(self.dealerCardList, 1)[0]
    self.dealer.append(d_card)
    self.d_point += d_card
    d_card = QPixmap(str(d_card) + "_r.jpg")
    d_lbl.setPixmap(d_card)
    d_lbl.setGeometry(self.d_previous + self.interval, 70, 60, 100)
    self.d_previous = self.d_previous + self.interval
    self.dealer_sum = sum(self.dealer)
    self.dealer_to_21 = 21 - self.dealer_sum
    time.sleep(1.0)
    d_lbl.show()
    self.showPoint()
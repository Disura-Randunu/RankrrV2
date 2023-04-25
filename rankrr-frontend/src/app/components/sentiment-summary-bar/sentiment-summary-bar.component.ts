import { Component, Input, OnInit, OnChanges} from '@angular/core';

@Component({
  selector: 'app-sentiment-summary-bar',
  templateUrl: './sentiment-summary-bar.component.html',
  styleUrls: ['./sentiment-summary-bar.component.css']
})
export class SentimentSummaryBarComponent implements OnChanges{
 
  @Input() negative: number
  @Input() neutral: number
  @Input() positive: number

  negativePercentage: string
  neutralPercentage: string
  positivePercentage: string

  ngOnChanges(): void {
    this.negativePercentage = `${this.negative.toFixed(2)}%`
    this.neutralPercentage = `${this.neutral.toFixed(2)}%`
    this.positivePercentage = `${this.positive.toFixed(2)}%`
  }

}

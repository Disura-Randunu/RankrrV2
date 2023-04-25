import { Component, OnInit } from '@angular/core';
import { TextAnalyzerService } from 'src/app/services/text-analyzer.service';
import { MessageService } from 'primeng/api';

@Component({
  selector: 'app-text-analyzer',
  templateUrl: './text-analyzer.component.html',
  styleUrls: ['./text-analyzer.component.css']
})
export class TextAnalyzerComponent implements OnInit {

  text: string = 'Design is somewhat normal. But the quality is so puuuuuurfecttt'
  analyzing: boolean = false

  ml = null;
  advanced = null;
  basic = null;
  constructor(private textAnalyzerService: TextAnalyzerService, private messageService: MessageService) {}

  ngOnInit(): void {
    
  }

  onSubmit(){
    if(!this.text){
      alert("Please enter the text to analyze")
      return
    }
    this.analyzing = true
    this.textAnalyzerService.getAnalyzedText(this.text).subscribe((data) => {
      this.messageService.add({ severity: 'success', summary: 'Success', detail: 'Text analyzing successfull' });
      this.analyzing = false
      this.ml = data.ml
      this.advanced = data.advanced
      this.basic = data.basic
      console.log(data)
    })
  }

  onAnalyze(text){
    this.textAnalyzerService.getAnalyzedText(text).subscribe((data) => {
      this.ml = data.ml
    })
  }

}

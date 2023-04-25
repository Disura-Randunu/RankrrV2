import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SentimentSummaryBarComponent } from './sentiment-summary-bar.component';

describe('SentimentSummaryBarComponent', () => {
  let component: SentimentSummaryBarComponent;
  let fixture: ComponentFixture<SentimentSummaryBarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SentimentSummaryBarComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SentimentSummaryBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

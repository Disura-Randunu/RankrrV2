import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TextAnalyzerComponent } from './text-analyzer.component';

describe('TextAnalyzerComponent', () => {
  let component: TextAnalyzerComponent;
  let fixture: ComponentFixture<TextAnalyzerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TextAnalyzerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TextAnalyzerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

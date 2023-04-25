import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RankerDemoComponent } from './ranker-demo.component';

describe('RankerDemoComponent', () => {
  let component: RankerDemoComponent;
  let fixture: ComponentFixture<RankerDemoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RankerDemoComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RankerDemoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

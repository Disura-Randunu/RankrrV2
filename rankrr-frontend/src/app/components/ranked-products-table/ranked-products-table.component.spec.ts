import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RankedProductsTableComponent } from './ranked-products-table.component';

describe('RankedProductsTableComponent', () => {
  let component: RankedProductsTableComponent;
  let fixture: ComponentFixture<RankedProductsTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RankedProductsTableComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RankedProductsTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

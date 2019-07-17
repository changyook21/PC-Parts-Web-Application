import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListSaleComponent } from './list-sale.component';

describe('DashboardSaleComponent', () => {
  let component: ListSaleComponent;
  let fixture: ComponentFixture<ListSaleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListSaleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListSaleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});

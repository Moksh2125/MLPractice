# All Columns — Sales & Inventory

Every column on every sales and inventory table, unfiltered — 70 tables, ~2,100 columns in total. See [SALES-INVENTORY-REFERENCE.md](SALES-INVENTORY-REFERENCE.md) for what they mean and which ones to actually test with; use this file when you need the exact, complete column list for a table.

## Sales tables — bills & item lines

**`fct_orders`** — one row per bill (every status — successful, cancelled, complimentary, advanced) (134 columns)

`order_key`, `restaurant_id`, `restaurant_key`, `unique_instance_id`, `restaurant_name`, `brand_name`, `virtual_brand`, `city_name`, `state_name`, `area_name`, `business_date`, `created_at`, `hour_of_day`, `hour_range_label`, `hour_12h_label`, `invoice_no`, `invoice_id`, `status_code`, `order_status_text`, `status_name`, `is_success`, `is_online`, `online_offline`, `channel_id`, `channel_name`, `order_type_code`, `order_type_name`, `order_mode_name`, `sub_order_type`, `bill_group_name`, `location_name`, `payment_type_code`, `payment_mode`, `custom_payment_type`, `payment_description`, `core_price_amount`, `discount_amount`, `tax_amount`, `after_discount_amount`, `bill_total`, `settled_amount`, `waived_off_amount`, `is_settled`, `roundoff_amount`, `total_without_tax_amount`, `packing_charge_amount`, `delivery_charge_amount`, `tip_amount`, `service_charge_amount`, `gst_paid_by_merchant_amount`, `gst_paid_by_ecommerce_amount`, `online_tax_calculated_amount`, `gst_merchant_on_items_amount`, `gst_merchant_on_packing_amount`, `gst_merchant_on_service_charge_amount`, `gst_ecommerce_on_items_amount`, `gst_ecommerce_on_packing_amount`, `gst_ecommerce_on_service_charge_amount`, `guests`, `customer_name`, `customer_phone`, `customer_key`, `customer_address`, `customer_locality`, `billing_user`, `waiter_name`, `cancel_reason`, `complimentary_reason`, `gst_no`, `b2b_b2c`, `table_no`, `coupon_code`, `print_count`, `is_changed_after_print`, `modified_at`, `remarks`, `cancelled_by`, `is_advance_order`, `aggregator_order_id`, `online_order_key`, `table_turnaround_time`, `order_uid`, `from_where`, `payment_collection_date`, `settle_total`, `has_positive_settlement`, `settled_including_zero_amount`, `settlement_adjustment_signed_amount`, `additional_charge_amount`, `deduction_charge_amount`, `additional_charge_legacy_amount`, `facilitator_id`, `counter_name`, `advance_order_date`, `entry_at`, `settled_by_name`, `billing_user_id`, `reservation_web_id`, `printed`, `offline_delivered_at`, `offline_returned_to_store_at`, `source_billing_user_name`, `source_amount_paid`, `source_roundoff`, `source_customer_id`, `source_customer_phone`, `source_payment_confirmation`, `source_desktop_datetime`, `source_old_customer_id`, `source_desktop_id`, `source_no_of_persons`, `source_finalized`, `source_order_edit_flag`, `source_is_consumed`, `source_restaurant_area_id`, `source_change_after_print`, `source_delivery_distance`, `source_old_pending_order_id`, `source_payment_reconciliation_id`, `source_packing_charge_calculation`, `source_bill_paid`, `source_extra_data`, `source_old_total`, `source_delivery_status`, `source_final_invoice`, `source_advance_order_flag`, `source_sub_order_type_id`, `source_lat`, `source_long`, `source_order_type_name`, `source_payment_type_name`, `source_pending_user_name`, `is_bogo_applied`, `bogo_offer_name`

**`fct_order_items`** — one row per item line on a bill (deleted items and tax rows are already removed) (55 columns)

`order_item_key`, `order_key`, `restaurant_id`, `restaurant_key`, `unique_instance_id`, `restaurant_name`, `brand_name`, `business_date`, `created_at`, `hour_of_day`, `invoice_no`, `status_code`, `status_name`, `is_success`, `is_online`, `online_offline`, `channel_id`, `channel_name`, `order_type_name`, `payment_mode`, `item_id`, `item_name`, `category_name`, `group_name`, `variation_name`, `addon_name`, `sap_code`, `item_code`, `hsn_code`, `bogo_id`, `bogo_price`, `is_bogo_free_item`, `discount_title`, `quantity`, `price`, `original_price`, `line_amount`, `line_discount_amount`, `line_tax_amount`, `line_packing_charge_amount`, `line_after_discount_amount`, `line_with_tax_amount`, `line_bill_amount`, `is_taxable`, `special_notes`, `billing_user`, `item_created_date`, `item_order_status`, `item_category_id`, `is_bogo_raw`, `discount_id`, `is_taxable_nonzero`, `is_non_taxable`, `is_tax_unknown`, `item_discount_details_json`

**`fct_order_item_taxes`** — one row per tax line on a bill (CGST, SGST, VAT…) (17 columns)

`tax_line_key`, `order_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `business_date`, `invoice_no`, `status_name`, `is_success`, `channel_name`, `tax_id`, `tax_name`, `tax_type`, `tax_percentage`, `tax_amount`, `taxable_amount`, `tax_on_charge_of_id`

**`fct_order_item_tax_splits`** — one row per tax on one item line, per source (an item line with CGST and SGST has two 'item' rows, plus a 'charges' row per tax when the bill taxes its packing) (26 columns)

`order_item_key`, `order_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `business_date`, `invoice_no`, `status_name`, `is_success`, `channel_name`, `item_id`, `item_name`, `category_name`, `group_name`, `hsn_code`, `quantity`, `line_after_discount_amount`, `tax_id`, `tax_name`, `tax_type`, `tax_percentage`, `item_tax_amount`, `tax_source`, `is_charge`, `is_unmapped_tax`, `has_conflicting_metadata`

**`fct_order_lines`** — one row per bill line record (items, taxes and charges) (order_items row as stored, every status) (56 columns)

`id`, `order_id`, `item_id`, `restaurant_id`, `restaurant_key`, `type`, `quantity`, `price`, `original_price`, `total_discount`, `total_tax`, `total`, `name`, `unit`, `fixed_per`, `created`, `modified`, `changed`, `old_item_id`, `desktop_id`, `special_notes`, `group_category_id`, `category_wise_taxes`, `discount_id`, `discount_total`, `discount_details`, `addons`, `packing_charge`, `item_extra_data`, `unique_instance_id`, `res_name`, `city_name`, `state_name`, `created_date`, `order_type`, `pending_order_user_id`, `client_identifier`, `brand_name`, `category_name`, `variation_name`, `hour_ordered`, `billing_user_name`, `table_no`, `sapcode`, `addon_name`, `group_name`, `deleted_items`, `order_status`, `order_type_name`, `is_eligible_item`, `line_kind`, `is_deleted_record`, `item_after_discount_amount`, `item_with_tax_amount`, `record_date`, `created_at`

**`fct_order_addons`** — one row per add-on on an item line of a bill (for example Extra Cheese on one Pizza line) (35 columns)

`order_addon_key`, `order_item_key`, `order_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `brand_name`, `virtual_brand`, `business_date`, `hour_of_day`, `invoice_no`, `status_name`, `is_success`, `is_online`, `channel_id`, `channel_name`, `order_type_name`, `item_id`, `item_name`, `category_name`, `group_name`, `variation_name`, `item_quantity`, `item_price`, `addon_group_name`, `addon_item_name`, `addon_sap_code`, `addon_price`, `addon_qty_per_item`, `addon_amount_per_item_unit`, `addon_quantity`, `addon_sales_amount`, `addon_status_code`, `addon_status_name`, `is_active_addon`

**`fct_order_discount_lines`** — one row per discount line on a bill (the name of a discount given, for example Special Discount) (15 columns)

`discount_line_key`, `order_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `business_date`, `invoice_no`, `status_name`, `is_success`, `channel_name`, `discount_name`, `discount_line_amount`, `special_notes`, `online_order_key`, `is_online`

**`fct_order_item_rollup`** — one row per bill (its item lines summed) (12 columns)

`restaurant_id`, `unique_instance_id`, `order_key`, `item_line_count`, `item_quantity`, `item_before_discount_amount`, `item_discount_amount`, `item_after_discount_amount`, `item_tax_amount`, `item_packing_amount`, `item_bill_amount`, `unknown_tax_line_count`

**`fct_order_staff_basic`** — one row per item line on a bill, with its billing user (17 columns)

`order_item_key`, `order_key`, `restaurant_id`, `unique_instance_id`, `business_date`, `restaurant_name`, `item_id`, `item_name`, `quantity`, `line_amount`, `is_success`, `billing_user_id`, `billing_user`, `facilitator_id`, `assigned_to`, `billing_user_display_name`, `billing_user_type_code`

**`fct_order_tax_metadata`** — one row per tax id on a bill (the bill's tax lines collapsed per tax id) (13 columns)

`restaurant_id`, `unique_instance_id`, `order_key`, `tax_id`, `tax_name`, `tax_type`, `tax_percentage`, `bill_tax_amount`, `tax_on_charge_of_id`, `is_tax_on_charge`, `is_charge`, `source_tax_line_count`, `has_conflicting_metadata`

**`agg_sales_daily`** — one row per outlet and day (the day's bills from fct_orders, summed) (18 columns)

`restaurant_id`, `unique_instance_id`, `business_date`, `all_status_bill_count`, `successful_bill_count`, `cancelled_bill_count`, `complimentary_bill_count`, `before_discount_amount`, `discount_amount`, `after_discount_amount`, `tax_amount`, `billed_amount`, `settled_amount`, `waived_off_amount`, `cancelled_amount`, `complimentary_amount`, `guests`, `missing_amount_bill_count`

## Sales tables — online orders, KOTs & payments

**`fct_online_orders`** — one row per online order received from an aggregator (Swiggy, Zomato…) or website, every status (79 columns)

`online_order_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `virtual_brand`, `business_date`, `is_in_report_dates`, `received_at`, `hour_of_day`, `aggregator_order_id`, `invoice_id`, `invoice_date`, `channel_id`, `channel_name`, `entry_type_code`, `entry_type_name`, `status_code`, `status_name`, `is_cancelled`, `is_advance_order`, `payment_type_code`, `payment_type_name`, `order_type_code`, `cancel_by_code`, `client_restaurant_id`, `preorder_at`, `order_total_amount`, `is_modified`, `is_auto_accepted`, `cancel_reason`, `device_type_code`, `device_type_name`, `modified_on_code`, `modified_on_name`, `customer_name`, `customer_phone`, `rider_name`, `rider_phone`, `rider_last_status`, `accepted_at`, `first_bill_generated_at`, `accept_date_type_at`, `rider_arrived_at`, `mark_ready_at`, `picked_up_at`, `delivered_at`, `cancelled_at`, `returned_to_store_at`, `acknowledge_seconds`, `preparation_seconds`, `cancel_seconds`, `food_prep_seconds`, `order_time_seconds`, `road_time_seconds`, `return_to_store_seconds`, `online_customer_address`, `is_train_order`, `source_desktop_id`, `source_user_name`, `source_order_json`, `source_mapped_order_json`, `source_advanced_order`, `source_is_modified`, `source_app_status`, `source_autoaccept`, `source_cancel_reason`, `source_history`, `source_udid`, `source_created`, `source_modified`, `source_minimum_delivery_time`, `source_minimum_prep_time`, `source_customer_phone`, `source_accept_date_type`, `source_notify_thirdparty`, `source_thirdparty_status`, `source_extra_data`, `source_insert_date`, `source_created_date`

**`fct_online_order_events`** — one row per status event of an online order (one entry of its history) (12 columns)

`online_order_key`, `restaurant_id`, `unique_instance_id`, `received_date`, `channel_id`, `event_offset`, `event_status_raw`, `event_status_code`, `event_at`, `rider_status`, `event_source_code`, `event_json`

**`fct_kots`** — one row per Kitchen Order Ticket (KOT); removed KOTs (status -9) are already left out (19 columns)

`kot_key`, `restaurant_id`, `restaurant_key`, `unique_instance_id`, `kot_no`, `order_key`, `bill_link_name`, `is_bill_generated`, `business_date`, `is_in_report_dates`, `created_at`, `hour_of_day`, `order_type_code`, `order_type_name`, `status_code`, `status_name`, `is_cancelled`, `print_count`, `marked_done_at`

**`fct_kot_items`** — one row per item line on a KOT, every item status (items of removed KOTs are already left out) (34 columns)

`kot_item_key`, `kot_key`, `kot_no`, `order_key`, `restaurant_id`, `unique_instance_id`, `business_date`, `is_in_report_dates`, `hour_of_day`, `order_type_name`, `kot_status_name`, `is_kot_cancelled`, `is_bill_generated`, `item_id`, `item_name`, `category_name`, `group_name`, `variation_name`, `item_code`, `sap_code`, `hsn_code`, `entry_type_code`, `quantity`, `price`, `line_amount`, `status_code`, `status_name`, `is_cancelled`, `special_notes`, `addons`, `received_at`, `preparation_started_at`, `prepared_at`, `preparation_minutes`

**`fct_kot_records`** — one row per KOT record (kots row as stored, every status) (44 columns)

`id`, `restaurant_id`, `restaurant_key`, `kot_id`, `billing_user_id`, `billing_user_name`, `billing_user_original_name`, `order_type`, `customer_id`, `customer_phone`, `customer_name`, `customer_address`, `customer_locality`, `table_no`, `status`, `done_by_preparer`, `cancel_by_preparer`, `created`, `modified`, `desktop_datetime`, `old_customer_id`, `desktop_id`, `order_id`, `old_order_id`, `facilitator_id`, `cancel_kot_description`, `pending_order_id`, `old_pending_order_id`, `print_count`, `description`, `no_of_persons`, `is_running`, `mark_as_done_date`, `extra_data`, `counter_name`, `is_informed`, `sub_order_type_id`, `unique_instance_id`, `is_deleted_record`, `is_cancelled_record`, `has_bill`, `record_date`, `created_at`, `status_name`

**`fct_kot_line_records`** — one row per KOT line record (kot_items row as stored, every status) (29 columns)

`id`, `kot_id`, `item_id`, `restaurant_id`, `restaurant_key`, `type`, `quantity`, `price`, `total`, `name`, `unit`, `created`, `modified`, `old_item_id`, `desktop_id`, `changed`, `status`, `preparation_starts`, `preparation_ends`, `special_notes`, `extra_data_json`, `addons`, `item_extra_data`, `unique_instance_id`, `is_cancelled_record`, `is_item_record`, `record_date`, `created_at`, `status_name`

**`fct_part_payments`** — one row per payment split of a Part Payment bill (one bill paid partly by cash, partly by card…) (25 columns)

`part_payment_key`, `order_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `brand_name`, `business_date`, `hour_of_day`, `invoice_no`, `status_code`, `status_name`, `is_success`, `is_online`, `channel_name`, `order_type_name`, `bill_total`, `payment_type_code`, `payment_mode`, `payment_method`, `payment_description`, `paid_amount`, `reference_no`, `is_due_payment`, `reference_amount`, `remaining_due_amount`

**`fct_payments`** — one row per payment row: a whole bill paid one way, or one split of a part-payment bill (31 columns)

`order_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `brand_name`, `business_date`, `hour_of_day`, `invoice_no`, `status_code`, `status_name`, `is_success`, `is_online`, `channel_name`, `order_type_name`, `bill_total`, `hour_12h_label`, `settled_amount`, `waived_off`, `settlement_adjustment_signed_amount`, `payment_type_code`, `payment_mode`, `payment_method`, `payment_description`, `paid_amount`, `billed_basis_amount`, `reference_no`, `reference_amount`, `is_due_payment`, `remaining_due_amount`, `is_part_payment`, `payment_row_key`

**`fct_payment_entries`** — one row per split payment (part_payments row as stored, every status) (21 columns)

`id`, `restaurant_id`, `restaurant_key`, `order_id`, `desktop_id`, `payment_method`, `payment_method_desc`, `payment_type`, `amount`, `extra_information`, `status`, `reference_no`, `reference_amount`, `created`, `modified`, `unique_instance_id`, `is_active_record`, `is_deleted_record`, `is_due_payment`, `payment_created_at`, `collected_date`

**`fct_payment_reconciliation`** — one row per bill, with its split payments summed (16 columns)

`order_key`, `restaurant_id`, `unique_instance_id`, `business_date`, `restaurant_name`, `status_code`, `is_success`, `payment_type_code`, `bill_total`, `settled_amount`, `split_count`, `null_split_amount_count`, `split_amount`, `is_missing_split`, `split_minus_billed_amount`, `split_minus_settled_amount`

**`fct_addon_entries`** — one row per add-on entry on a bill line (orderwise_addons row as stored, every status) (33 columns)

`id`, `restaurant_id`, `restaurant_key`, `order_id`, `order_item_id`, `addon_group_id`, `addon_group_name`, `addon_item_id`, `addon_item_name`, `addon_item_price`, `addon_item_qty`, `changed`, `status`, `is_consumed`, `sap_code`, `created`, `modified`, `unique_instance_id`, `res_name`, `city_name`, `state_name`, `created_date`, `order_type`, `pending_order_user_id`, `client_identifier`, `brand_name`, `item_id`, `parent_addon_id`, `is_active_record`, `amount_per_parent_unit`, `record_date`, `created_at`, `addon_status_name`

## Sales tables — menu, people & operations

**`dim_menu_items`** — one row per menu record in the item master (menu items, semi cooked and raw items; base items and their variation rows), every status (47 columns)

`item_id`, `restaurant_id`, `category_id`, `item_name`, `online_display_name`, `item_code`, `description`, `item_type_code`, `item_type_name`, `is_menu_item`, `status_code`, `status_name`, `is_active`, `in_stock_code`, `in_stock_name`, `is_in_stock`, `price_amount`, `packing_charge_amount`, `order_type_codes`, `attribute_ids`, `food_type`, `parent_item_id`, `is_variation`, `variation_id`, `has_variations`, `has_addons`, `addon_level_code`, `addon_level_name`, `addon_group_ids`, `is_tax_ignored`, `hsn_code`, `has_own_recipe`, `incentive_type_code`, `incentive_type_name`, `incentive_value`, `minimum_stock`, `maximum_stock`, `at_par_stock`, `is_favorite`, `display_rank`, `zomato_image`, `swiggy_image`, `other_platforms_image`, `ho_record_id`, `is_from_ho`, `created_at`, `modified_at`

**`dim_categories`** — one row per menu category, every status (17 columns)

`category_id`, `restaurant_id`, `category_name`, `tags`, `parent_category_id`, `parent_category_name`, `status_code`, `status_name`, `is_active`, `display_rank`, `zomato_logo`, `swiggy_logo`, `other_platforms_logo`, `ho_record_id`, `is_from_ho`, `created_at`, `modified_at`

**`dim_group_categories`** — one row per group category and category (the group's category list is already split into one row per category) (12 columns)

`group_category_id`, `restaurant_id`, `group_category_name`, `category_id`, `status_code`, `status_name`, `is_active`, `display_rank`, `ho_record_id`, `is_from_ho`, `created_at`, `modified_at`

**`dim_variations`** — one row per variation (for example Half, Full, 500 ml), every status (15 columns)

`variation_id`, `restaurant_id`, `variation_name`, `online_name`, `online_group_label`, `status_code`, `status_name`, `is_active`, `display_rank`, `attribute_code`, `food_type`, `ho_record_id`, `is_from_ho`, `created_at`, `modified_at`

**`dim_addon_groups`** — one row per add-on group (for example Choice Of Preparation), every status (17 columns)

`addon_group_id`, `restaurant_id`, `addon_group_name`, `online_display_name`, `selection_type_code`, `selection_type_name`, `min_quantity`, `max_quantity`, `is_shown_in_pos`, `is_shown_online`, `is_shown_in_captain_app`, `status_code`, `status_name`, `is_active`, `display_rank`, `created_at`, `modified_at`

**`dim_addon_items`** — one row per add-on item row (for example Cheese Burst), every status (19 columns)

`addon_item_id`, `restaurant_id`, `addon_group_id`, `restaurant_area_id`, `addon_item_name`, `price_amount`, `addon_type_code`, `addon_type_name`, `status_code`, `status_name`, `is_active`, `display_rank`, `attribute_code`, `food_type`, `image`, `ho_record_id`, `is_from_ho`, `created_at`, `modified_at`

**`dim_item_taxes`** — one row per item-tax rule and item (the rule's item list is already split into one row per item) (13 columns)

`item_tax_id`, `restaurant_id`, `tax_id`, `tax_name`, `tax_rate`, `tax_rate_kind`, `tax_is_active`, `restaurant_area_id`, `item_id`, `ho_record_id`, `is_from_ho`, `created_at`, `modified_at`

**`dim_customers`** — one row per customer record of a restaurant (CRM customer master), every status (28 columns)

`customer_key`, `restaurant_id`, `restaurant_name`, `customer_name`, `customer_phone`, `alternate_phone`, `customer_email`, `customer_address`, `customer_locality`, `latitude`, `longitude`, `gst_no`, `date_of_birth`, `anniversary_date`, `is_dnd`, `is_favorite`, `status_code`, `status_name`, `is_deleted`, `source_code`, `source_name`, `aggregator_id`, `aggregator_name`, `customer_tag_ids`, `discount_details`, `created_at`, `created_date`, `modified_at`

**`dim_customer_records`** — one row per customer record (customers row as stored, every status) (31 columns)

`id`, `restaurant_id`, `name`, `phone`, `address`, `locality`, `phone1`, `email`, `dnd`, `favorite`, `discount_details`, `gst_no`, `fav_item_json`, `latitude`, `longitude`, `status`, `created`, `modified`, `desktop_datetime`, `due_total`, `from_where`, `customer_tag_ids`, `from_username`, `from_userid`, `DOB`, `ANNIVERSARY`, `created_date`, `is_deleted_record`, `is_active_record`, `created_at`, `status_name`

**`dim_staff`** — one row per staff user of a restaurant (billing user, delivery boy, waiter, captain, online acceptance app, delivery chain), every status (13 columns)

`staff_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `staff_name`, `staff_phone`, `staff_type_code`, `staff_type_name`, `status_code`, `status_name`, `is_active`, `created_at`, `created_date`

**`dim_staff_records`** — one row per staff (billing user) record (billing_users row as stored, every status) (20 columns)

`id`, `restaurant_id`, `user_id`, `user_type`, `user_name`, `user_code`, `name`, `phone`, `masters`, `status`, `created_by_id`, `report_rights`, `configurations`, `billing_user_group_id`, `created`, `modified`, `unique_instance_id`, `is_active_record`, `created_at`, `status_name`

**`dim_restaurant_areas`** — one row per area inside a restaurant (for example AC Hall, Garden, or an online platform area), every status (12 columns)

`restaurant_area_id`, `restaurant_id`, `area_id`, `area_name`, `status_code`, `status_name`, `is_active`, `display_rank`, `ho_record_id`, `is_from_ho`, `created_at`, `modified_at`

**`dim_restaurant_tables`** — one row per seating table in a restaurant, every status (13 columns)

`table_id`, `restaurant_id`, `restaurant_area_id`, `table_no`, `seating_capacity`, `status_code`, `status_name`, `is_active`, `display_rank`, `waiter_device_id`, `waiter_device_battery_percent`, `created_at`, `modified_at`

**`fct_item_availability_logs`** — one row per on/off log of an item, add-on or whole store on an online platform (one off period) (33 columns)

`availability_log_key`, `restaurant_id`, `unique_instance_id`, `virtual_brand`, `channel_name`, `entity_type_code`, `entity_type_name`, `item_id`, `item_name`, `category_id`, `category_name`, `trigger_type_code`, `trigger_type_name`, `is_on`, `availability_name`, `business_date`, `off_start_date`, `off_start_at`, `scheduled_on_at`, `turned_on_at`, `off_end_at`, `off_duration_minutes`, `off_duration_from_created_minutes`, `created_at`, `source_client_restaurant_id`, `source_user_name`, `source_mapped_id`, `source_on_date`, `source_is_on`, `source_off_from_date`, `source_off_to_date`, `source_modified`, `source_is_cron`

**`fct_day_ends`** — one row per restaurant business day (only the latest day-end record of each day) (16 columns)

`day_end_key`, `restaurant_id`, `unique_instance_id`, `business_date`, `day_end_at`, `status_code`, `status_name`, `is_day_closed`, `previous_closing_balance_amount`, `closing_balance_amount`, `day_start_petty_cash_amount`, `day_end_petty_cash_amount`, `recorded_sales_amount`, `recorded_expense_amount`, `recorded_withdrawal_amount`, `day_end_details_json`

**`fct_day_end_records`** — one row per day-end record (repeats of a day included) (day_ends row as stored, every status) (28 columns)

`id`, `restaurant_id`, `day_start_date`, `day_start_admin_id`, `day_start_admin_details`, `day_end_admin_id`, `day_end_admin_details`, `prev_closing_balance`, `total_expense`, `total_withdrawal`, `total_withdrawal_details`, `total_sales`, `current_closing_balance`, `day_end_date`, `status`, `extra_data`, `day_start_pettycash_amount`, `day_end_pettycash_amount`, `desktop_id`, `send_flag`, `created`, `modified`, `unique_instance_id`, `is_day_closed`, `recorded_balance_change`, `record_date`, `created_at`, `status_name`

**`fct_expenses`** — one row per expense, withdrawal or top-up entry, active and deleted (25 columns)

`expense_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `brand_name`, `city_name`, `state_name`, `business_date`, `expense_category_id`, `expense_category_name`, `billing_user_id`, `description`, `entry_type_code`, `entry_type_name`, `status_code`, `status_name`, `is_deleted`, `transaction_amount`, `paid_from_code`, `paid_from_name`, `created_at`, `modified_at`, `source_desktop_id`, `source_expense_date`, `source_desktop_datetime`

**`dim_expense_categories_records`** — one row per expense category (expense master) record (expense_master row as stored, every status) (10 columns)

`id`, `restaurant_id`, `title`, `status`, `type`, `created`, `modified`, `is_active_record`, `is_deleted_record`, `created_at`

**`fct_zomato_ratings`** — one row per Zomato rating received (13 columns)

`restaurant_id`, `aggregator_order_id`, `client_restaurant_id`, `virtual_brand`, `rating`, `feedback`, `customer_name`, `business_date`, `created_at`, `modified_at`, `item_details_json`, `source_client_order_id`, `source_rating`

## Inventory tables — purchasing & purchase orders

**`fct_purchases`** — one row per inward stock entry (purchase_master header) — purchase, internal transfer in, manual stock, sale return, old transfer, unit conversion; every status (59 columns)

`purchase_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `business_date`, `created_at`, `movement_type_code`, `movement_type_name`, `source_stock_outward_key`, `po_type_code`, `po_type_name`, `receiver_id`, `receiver_type_code`, `receiver_type_name`, `receiver_name`, `invoice_number`, `mrn_no`, `gst_no`, `status_code`, `record_status_code`, `status_name`, `is_active`, `is_saved`, `is_sent`, `is_processed`, `is_in_stock_movement`, `is_stock_updated`, `total_amount`, `roundoff_amount`, `tax_amount`, `discount_amount`, `discount_type_code`, `discount_type_name`, `discount_value`, `delivery_charge_amount`, `paid_amount`, `is_paid`, `payment_status_name`, `payment_date`, `payment_mode_code`, `payment_mode_name`, `created_by_user`, `cancel_reason`, `transport_no`, `modified_at`, `lifecycle_status_name`, `is_processed_document`, `po_reference_number`, `tcs_amount`, `tds_amount`, `delivery_cgst_amount`, `delivery_sgst_amount`, `delivery_igst_amount`, `delivery_vat_amount`, `business_type`, `receiver_contact`, `receiver_email`, `receiver_address`, `receiver_gst_no`

**`fct_purchase_items`** — one row per raw material line on an inward stock entry (purchase, internal transfer in, manual stock, sale return…) (60 columns)

`purchase_item_key`, `purchase_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `business_date`, `movement_type_code`, `movement_type_name`, `receiver_id`, `receiver_type_name`, `receiver_name`, `invoice_number`, `status_name`, `is_active`, `is_saved`, `is_sent`, `is_in_stock_movement`, `is_stock_updated`, `line_status_code`, `is_line_active`, `raw_material_id`, `raw_material_name`, `raw_material_category`, `hsn_code`, `unit_id`, `unit_name`, `qty`, `purchase_unit_id`, `purchase_unit_name`, `consumption_unit_id`, `consumption_unit_name`, `conversion_qty`, `qty_in_consumption_unit`, `qty_in_purchase_unit`, `price`, `weighted_price`, `line_amount`, `line_discount_amount`, `cgst_percent`, `sgst_percent`, `igst_percent`, `vat_or_cess_percent`, `cgst_amount`, `sgst_amount`, `igst_amount`, `vat_or_cess_amount`, `line_tax_amount`, `expiry_date`, `created_at`, `qty_in_consumption_unit_strict`, `qty_in_purchase_unit_strict`, `can_convert_to_consumption_unit`, `can_convert_to_purchase_unit`, `lifecycle_status_name`, `is_processed_document`, `line_total_including_tax_amount`, `source_line_status_code`, `normal_loss_percent_source`, `normal_loss_qty_consumption_unit`, `normal_loss_qty_purchase_unit`

**`fct_purchase_payments`** — one row per payment made against a purchase, paid in the report period (13 columns)

`purchase_payment_key`, `purchase_key`, `restaurant_id`, `unique_instance_id`, `payment_date`, `payment_mode_code`, `payment_mode_name`, `payment_reference_no`, `paid_amount`, `status_code`, `is_active`, `created_at`, `modified_at`

**`fct_purchase_batches`** — one row per purchased batch of a raw material (28 columns)

`batch_key`, `purchase_key`, `purchase_line_key`, `restaurant_id`, `unique_instance_id`, `movement_type_code`, `raw_material_id`, `raw_material_name`, `batch_no`, `invoice_date`, `invoice_no`, `manufacturing_date`, `expiry_date`, `days_to_expiry`, `tracks_expiry`, `qty_consumption_unit`, `remaining_qty_consumption_unit`, `consumption_unit_name`, `qty_purchase_unit`, `purchase_unit_name`, `conversion_qty`, `price_per_unit`, `weighted_price`, `sap_group_master_id`, `status_code`, `is_active`, `created_by_user`, `created_at`

**`fct_po_requests`** — one row per purchase order request (PO) raised by a restaurant to a supplier, central kitchen or store; every status (29 columns)

`po_request_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `business_date`, `created_at`, `request_number`, `receiver_id`, `receiver_type_code`, `receiver_type_name`, `receiver_name`, `raw_material_category`, `status_code`, `record_status_code`, `status_name`, `is_saved`, `is_sent`, `is_processed`, `is_open`, `total_amount`, `roundoff_amount`, `tax_amount`, `paid_amount`, `is_paid`, `payment_date`, `payment_mode_code`, `payment_mode_name`, `is_read`, `created_by_user`

**`fct_po_request_items`** — one row per raw material requested on a purchase order request (unpacked from the PO's item_details list) (30 columns)

`po_request_key`, `line_no`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `business_date`, `request_number`, `receiver_id`, `receiver_type_name`, `receiver_name`, `status_name`, `is_saved`, `is_sent`, `is_processed`, `is_open`, `raw_material_id`, `raw_material_name`, `raw_material_category`, `raw_material_sub_category`, `hsn_code`, `sap_code`, `description`, `unit_id`, `unit_name`, `requested_qty`, `consumption_unit_id`, `conversion_qty`, `requested_qty_in_consumption_unit`, `price`, `line_amount`

**`dim_suppliers`** — one row per supplier of a restaurant in scope (26 columns)

`supplier_id`, `restaurant_id`, `unique_instance_id`, `ho_record_id`, `supplier_name`, `company_name`, `gst_no`, `business_type`, `pan_no`, `tan_no`, `fssai_no`, `tcs_percent`, `phone`, `email`, `address`, `city`, `state`, `pin_code`, `shipping_address`, `shipping_city`, `shipping_state`, `supplier_type_code`, `status_code`, `is_active`, `created_at`, `modified_at`

**`fct_inventory_purchase_records`** — one row per inward (purchase) document record (purchase_master row as stored, every status) (50 columns)

`id`, `restaurant_id`, `type`, `po_id`, `po_type`, `receiver_id`, `receiver_type`, `ship_bill_outlet_id`, `sap_group_master_id`, `invoice_date`, `invoice_number`, `mrn_no`, `change_details`, `item_details`, `total`, `roundoff`, `paid_amount`, `record_status`, `status`, `update_stock`, `payment_flag`, `payment_date`, `payment_mode`, `gst_no`, `total_tax`, `total_discount`, `discount_type`, `discount_per`, `delivery_charge`, `delivery_charge_details`, `name`, `rest_details`, `tax_details`, `created_by`, `createdby_user_type`, `createdby_username`, `cancel_reason`, `created`, `modified`, `unique_instance_id`, `res_name`, `brand_name`, `state_name`, `city_name`, `invoice_file`, `tp_no`, `record_date`, `created_at`, `status_name`, `lifecycle_status_name`

**`fct_inventory_purchase_line_records`** — one row per inward (purchase) line record (purchase_item_details row as stored, every status) (34 columns)

`id`, `restaurant_id`, `purchase_id`, `item_id`, `unit`, `qty`, `price`, `weighted_price`, `amount`, `discount`, `tax1`, `tax2`, `tax3`, `tax4`, `tax1_amount`, `tax2_amount`, `tax3_amount`, `tax4_amount`, `hsn_code`, `description`, `actual_qty`, `actual_unit_id`, `actual_unit_name`, `status`, `expiry_date`, `created`, `modified`, `wastage_expiry_status`, `sale_id`, `unique_instance_id`, `category`, `item_extra_info`, `record_date`, `created_at`

**`fct_inventory_po_records`** — one row per purchase order request record (po_requests row as stored, every status) (39 columns)

`id`, `restaurant_id`, `receiver_id`, `receiver_type`, `ship_bill_outlet_id`, `sap_group_master_id`, `request_date`, `request_number`, `mrn_no`, `change_details`, `item_details`, `total`, `roundoff`, `total_tax`, `terms_of_payment`, `terms_of_delivery`, `rm_category`, `ship_to_bill_to_total`, `record_status`, `status`, `is_view`, `name`, `rest_details`, `is_editable`, `created_by`, `createdby_user_type`, `createdby_username`, `created`, `modified`, `type`, `unique_instance_id`, `paid_amount`, `payment_date`, `payment_flag`, `payment_mode`, `payment_ref_no`, `record_date`, `created_at`, `status_name`

## Inventory tables — stock & outward movement

**`fct_closing_stocks`** — one row per raw material per end-of-day stock snapshot (system closing stock of that day) (33 columns)

`closing_stock_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `snapshot_date`, `opening_for_date`, `is_opening_snapshot`, `is_closing_snapshot`, `created_at`, `raw_material_id`, `raw_material_name`, `raw_material_category`, `department_name`, `unit_id`, `unit_name`, `qty`, `avg_purchase_price`, `stock_value_amount`, `purchase_unit_id`, `purchase_unit_name`, `consumption_unit_id`, `consumption_unit_name`, `conversion_qty`, `qty_in_consumption_unit`, `avg_purchase_price_adjusted`, `qty_in_consumption_unit_strict`, `qty_in_purchase_unit_strict`, `can_convert_to_consumption_unit`, `can_convert_to_purchase_unit`, `sap_group_master_id`, `digital_stock_qty`, `digital_stock_avg_purchase_price`, `price_per_consumption_unit`

**`dim_stock_levels`** — one row per raw material with its CURRENT (live) stock balance — today's position, not a past date (36 columns)

`stock_level_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `raw_material_id`, `raw_material_name`, `raw_material_category`, `department_name`, `unit_id`, `unit_name`, `current_qty`, `previous_qty`, `purchase_unit_id`, `purchase_unit_name`, `consumption_unit_id`, `consumption_unit_name`, `conversion_qty`, `current_qty_in_consumption_unit`, `minimum_stock`, `at_par_stock`, `avg_purchase_price`, `avg_purchase_price_without_tax`, `current_stock_value_amount`, `last_item_purchase_price`, `last_purchase_price`, `avg_price_0_days`, `avg_price_15_days`, `avg_price_30_days`, `avg_price_45_days`, `avg_price_60_days`, `avg_price_75_days`, `avg_price_90_days`, `stock_updated_at`, `created_at`, `modified_at`, `sap_group_master_id`

**`fct_stock_outward`** — one row per outward stock entry (inventory sales header) — dispatch, purchase return, wastage, internal transfer out, manual stock; every status. NOT POS bills. (57 columns)

`stock_outward_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `business_date`, `created_at`, `movement_type_code`, `movement_type_name`, `restaurant_type_code`, `restaurant_type_name`, `sender_id`, `sender_type_code`, `sender_type_name`, `po_request_key`, `invoice_number`, `gst_no`, `raw_material_category`, `status_code`, `record_status_code`, `status_name`, `is_active`, `is_saved`, `is_sent`, `is_processed`, `is_in_stock_movement`, `is_stock_updated`, `total_amount`, `roundoff_amount`, `tax_amount`, `discount_amount`, `discount_type_code`, `discount_type_name`, `discount_value`, `delivery_charge_amount`, `paid_amount`, `is_paid`, `payment_date`, `payment_mode_code`, `payment_mode_name`, `created_by_user`, `cancel_reason`, `lifecycle_status_name`, `is_processed_document`, `po_reference_number`, `tcs_amount`, `tds_amount`, `delivery_cgst_amount`, `delivery_sgst_amount`, `delivery_igst_amount`, `delivery_vat_amount`, `business_type`, `receiver_name`, `receiver_city`, `receiver_contact`, `receiver_email`, `receiver_address`, `receiver_gst_no`

**`fct_stock_outward_items`** — one row per active raw material line on an outward stock entry (inactive lines are already removed) (63 columns)

`stock_outward_item_key`, `stock_outward_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `business_date`, `movement_type_code`, `movement_type_name`, `sender_id`, `sender_type_name`, `po_request_key`, `invoice_number`, `status_name`, `is_active`, `is_saved`, `is_sent`, `is_processed`, `is_in_stock_movement`, `is_stock_updated`, `raw_material_id`, `raw_material_name`, `raw_material_category`, `hsn_code`, `description`, `unit_id`, `unit_name`, `qty`, `purchase_unit_id`, `purchase_unit_name`, `consumption_unit_id`, `consumption_unit_name`, `conversion_qty`, `qty_in_consumption_unit`, `qty_in_purchase_unit`, `actual_qty`, `actual_unit_id`, `actual_unit_name`, `price`, `weighted_price`, `weighted_value_amount`, `line_amount`, `line_discount_amount`, `cgst_percent`, `sgst_percent`, `igst_percent`, `cess_percent`, `cgst_amount`, `sgst_amount`, `igst_amount`, `cess_amount`, `line_tax_amount`, `expiry_date`, `net_weight`, `manufacturing_date`, `created_at`, `qty_in_consumption_unit_strict`, `qty_in_purchase_unit_strict`, `can_convert_to_consumption_unit`, `can_convert_to_purchase_unit`, `lifecycle_status_name`, `is_processed_document`, `line_total_including_tax_amount`, `source_line_status_code`

**`fct_inventory_stock_records`** — one row per stock master record (current balance) (stock_masters row as stored, every status) (27 columns)

`id`, `restaurant_id`, `item_id`, `item_name`, `unit`, `unit_name`, `sap_group_master_id`, `department_name`, `qty`, `previous_qty`, `avg_purchase_price`, `last_item_purchase_price`, `last_purchase_price`, `stock_update_date`, `created`, `modified`, `days0`, `days15`, `days30`, `days45`, `days60`, `days75`, `days90`, `unique_instance_id`, `extra_info`, `avg_purchase_price_without_tax`, `created_at`

**`fct_inventory_snapshot_records`** — one row per closing stock snapshot record (closing_stocks row as stored, every status) (26 columns)

`id`, `restaurant_id`, `item_id`, `unit`, `sap_group_master_id`, `qty`, `avg_purchase_price`, `last_item_purchase_price`, `last_purchase_price`, `created`, `modified`, `item_name`, `unit_name`, `department_name`, `stock_qty`, `stock_avg_purchase_price`, `days0`, `days15`, `days30`, `days45`, `days60`, `days75`, `days90`, `unique_instance_id`, `record_date`, `created_at`

**`fct_inventory_movement_lines`** — one row per stock movement line — inward, outward or POS consumption — in a common consumption unit (23 columns)

`event_source`, `event_uid`, `source_row_key`, `document_key`, `restaurant_id`, `unique_instance_id`, `business_date`, `raw_material_id`, `raw_material_name`, `source_unit_id`, `source_qty`, `consumption_unit_id`, `qty_in_consumption_unit_strict`, `signed_qty_consumption_unit`, `can_convert_to_consumption_unit`, `movement_type_code`, `source_amount`, `legacy_policy_eligible`, `pos_order_status_code`, `lifecycle_status_name`, `is_processed_document`, `is_stock_updated`, `source_line_status_code`

**`fct_inventory_dispatch_records`** — one row per outward (dispatch) document record (sales row as stored, every status) (52 columns)

`id`, `restaurant_id`, `restaurant_type`, `type`, `sender_id`, `sender_type`, `ship_bill_outlet_id`, `sap_group_master_id`, `po_id`, `invoice_date`, `invoice_number`, `mrn_no`, `change_details`, `item_details`, `total`, `roundoff`, `record_status`, `status`, `update_stock`, `paid_amount`, `payment_date`, `payment_mode`, `gst_no`, `total_tax`, `total_discount`, `discount_type`, `discount_per`, `delivery_charge`, `delivery_charge_details`, `payment_flag`, `invoice_rcm_flag`, `invoice_terms_and_conditions`, `account_details`, `address`, `name`, `rest_details`, `tax_details`, `einvoice_details`, `ewaybill_details`, `created_by`, `createdby_user_type`, `createdby_username`, `cancel_reason`, `is_editable`, `created`, `modified`, `unique_instance_id`, `rm_category`, `record_date`, `created_at`, `status_name`, `lifecycle_status_name`

**`fct_inventory_dispatch_line_records`** — one row per outward (dispatch) line record (sale_item_details row as stored, every status) (32 columns)

`id`, `restaurant_id`, `sale_id`, `item_id`, `unit`, `qty`, `price`, `weighted_price`, `amount`, `discount`, `tax1`, `tax2`, `tax3`, `tax4`, `tax1_amount`, `tax2_amount`, `tax3_amount`, `tax4_amount`, `hsn_code`, `description`, `actual_qty`, `actual_unit_id`, `actual_unit_name`, `status`, `expiry_date`, `created`, `modified`, `unique_instance_id`, `category`, `item_extra_info`, `record_date`, `created_at`

## Inventory tables — consumption, recipes & raw materials

**`fct_pos_consumption`** — one row per raw material consumed by one POS order line, worked out from the recipe when the order was placed (every order status) (55 columns)

`consumption_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `business_date`, `created_at`, `consumption_type_code`, `consumption_type_name`, `order_key`, `invoice_id`, `order_type_code`, `order_type_name`, `order_area_id`, `table_no`, `payment_type_code`, `order_status_code`, `order_status_name`, `is_order_success`, `menu_item_id`, `menu_item_name`, `menu_item_qty`, `addon_id`, `addon_name`, `raw_material_id`, `raw_material_name`, `raw_material_category`, `unit_id`, `unit_name`, `qty`, `purchase_unit_id`, `purchase_unit_name`, `consumption_unit_id`, `consumption_unit_name`, `conversion_qty`, `qty_in_consumption_unit`, `qty_in_purchase_unit`, `avg_purchase_price`, `cost_amount`, `order_from`, `days0_cost_amount`, `days15_cost_amount`, `days30_cost_amount`, `days45_cost_amount`, `days60_cost_amount`, `days75_cost_amount`, `days90_cost_amount`, `selling_price`, `selling_amount`, `qty_in_consumption_unit_strict`, `qty_in_purchase_unit_strict`, `can_convert_to_consumption_unit`, `can_convert_to_purchase_unit`, `is_non_dispatch_consumption`, `sap_group_master_id`, `department_name`

**`fct_consumption_batches`** — one row per batch drawn by a consumption, in the report period (24 columns)

`consumption_batch_key`, `consumption_key`, `batch_reference_key`, `restaurant_id`, `unique_instance_id`, `consumed_from_code`, `raw_material_id`, `raw_material_name`, `invoice_no`, `invoice_date`, `expiry_date`, `tracks_expiry`, `qty_consumption_unit`, `remaining_qty_consumption_unit`, `consumption_unit_name`, `actual_qty`, `actual_unit_name`, `conversion_qty`, `price_per_unit`, `sap_group_master_id`, `status_code`, `is_active`, `consumed_date`, `created_at`

**`fct_inventory_consumption_records`** — one row per consumption record (consumed_item_details row as stored, every status) (33 columns)

`id`, `restaurant_id`, `type`, `order_id`, `invoice_id`, `sap_group_master_id`, `order_type`, `order_area`, `table_no`, `payment_type`, `order_from`, `order_created_date`, `order_status`, `item_id`, `item_name`, `item_qty`, `addon_id`, `addon_name`, `recipe_item_id`, `recipe_item_name`, `qty`, `unit`, `unit_name`, `price`, `cost`, `order_info`, `created`, `modified`, `is_update`, `department_name`, `unique_instance_id`, `record_date`, `created_at`

**`dim_raw_materials`** — one row per raw material (ingredient or semi cooked item) of a restaurant; deleted ones already removed (49 columns)

`raw_material_id`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `head_office_id`, `raw_material_name`, `short_name`, `raw_material_type_code`, `raw_material_type_name`, `raw_material_category`, `raw_material_sub_category`, `brand`, `description`, `status_code`, `status_name`, `is_active`, `purchase_unit_id`, `purchase_unit_name`, `consumption_unit_id`, `consumption_unit_name`, `conversion_qty`, `minimum_stock`, `minimum_stock_unit_id`, `maximum_stock`, `at_par_stock`, `at_par_stock_unit_id`, `stock_calculated_on_codes`, `hsn_code`, `sap_code`, `gtin`, `purchase_price`, `sale_price`, `reconciliation_price`, `tax_type_code`, `tax_type_name`, `gst_percent`, `is_in_cess_tax`, `cess_tax_percent`, `excise_duty`, `yield_loss_percent`, `consumption_type_code`, `consumption_type_name`, `has_expiry`, `is_private`, `is_decimal_qty_allowed`, `is_used_for_item_on_off`, `created_at`, `modified_at`, `created_by_user`

**`dim_recipes`** — one row per ingredient line of a recipe — one raw material and its quantity for one serving of a menu item or addon (30 columns)

`recipe_line_key`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `head_office_id`, `recipe_for_code`, `recipe_for_name`, `menu_item_id`, `menu_item_name`, `item_id`, `addon_id`, `raw_material_id`, `raw_material_name`, `raw_material_category`, `unit_id`, `unit_name`, `recipe_qty`, `consumption_unit_id`, `consumption_unit_name`, `conversion_qty`, `recipe_qty_in_consumption_unit`, `display_unit_id`, `display_qty`, `recipe_area_id`, `added_from_code`, `added_from_name`, `is_alternate_recipe_allowed`, `created_at`, `modified_at`, `created_by_user`

**`dim_inventory_raw_material_records`** — one row per raw material record (raw_materials row as stored, every status) (57 columns)

`id`, `restaurant_id`, `ho`, `name`, `short_name`, `type`, `unit1`, `consumption_unit`, `conversion_qty`, `unit`, `old_unit`, `description`, `minimum_stock`, `maximum_stock`, `at_par_stock`, `status`, `configuration`, `hsn_code`, `sap_code`, `price`, `sale_price`, `reconciliation_price`, `gst_per`, `favorite`, `category`, `yield_qty`, `standard_qty`, `at_par_stock_unit`, `minimum_stock_unit`, `calculated_on`, `container_info`, `is_in_cess_tax`, `cess_tax_percentage`, `is_private`, `tax_type`, `excise_duty`, `consumption_type`, `created`, `modified`, `created_by`, `createdby_username`, `is_expiry`, `desktop_datetime`, `old_id`, `is_update`, `unique_instance_id`, `use_in_item_onoff`, `min_qty`, `min_qty_unit`, `qty`, `gtin`, `brand`, `sub_category`, `sub_categorywise_rm_rank`, `allow_decimal_qty`, `created_at`, `status_name`

**`dim_inventory_recipe_records`** — one row per recipe line record (recipe_masters row as stored, every status) (22 columns)

`id`, `restaurant_id`, `ho`, `recipe_for`, `parent_item_id`, `addon_id`, `sap_group_master_id`, `item_id`, `recipe_item_id`, `recipe_item_unit`, `recipe_item_qty`, `recipe_item_area`, `added_from`, `created`, `modified`, `created_by`, `createdby_username`, `unique_instance_id`, `display_unit`, `display_qty`, `allow_alternate_recipe`, `created_at`

**`dim_inventory_menu_items`** — one row per menu item (id and name only), from the inventory copy of items_new (4 columns)

`menu_item_id`, `restaurant_id`, `restaurant_name`, `menu_item_name`

**`dim_inventory_units`** — one row per unit of measurement (Kg, GMS, CAS, Pcs…) set up for a restaurant (8 columns)

`unit_id`, `restaurant_id`, `unique_instance_id`, `restaurant_name`, `unit_name`, `head_office_id`, `created_at`, `modified_at`

**`dim_inventory_unit_records`** — one row per unit of measure record (restaurant_units row as stored, every status) (9 columns)

`id`, `restaurant_id`, `master_unit_id`, `display_name`, `ho`, `created`, `modified`, `unique_instance_id`, `created_at`

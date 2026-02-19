# good_example.tf — The same task, done right.
#
# Compare this to manual_dns.py and ask yourself:
# Which approach would you trust in production?

resource "bloxone_dns_a_record" "app_records" {
  for_each = {
    webserver = "10.100.10.50"
    dbserver  = "10.100.20.50"
    appserver = "10.100.10.51"
  }

  name_in_zone = each.key
  zone         = bloxone_dns_auth_zone.main.id
  rdata = {
    address = each.value
  }

  comment = "Managed by Terraform - ${var.environment}"

  # Idempotent    — run 100 times, same result
  # State tracked — Terraform knows exactly what exists
  # Drift detect  — catches manual portal changes automatically
  # Audit trail   — every change is a Git commit
  # Rollback      — git revert + terraform apply
  # Multi-env     — same code, different variables per environment
}

# What about IP allocation?
# Instead of a spreadsheet, use Infoblox as the source of truth:

# data "bloxone_ipam_next_available_ips" "auto" {
#   ip_space_id = bloxone_ipam_ip_space.main.id
#   subnet_id   = bloxone_ipam_subnet.app.id
#   count       = 3
# }
#
# No spreadsheet. No collisions. No "verbal agreements."
# The API guarantees uniqueness. Every time.

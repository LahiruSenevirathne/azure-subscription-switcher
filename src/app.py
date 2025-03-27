import json
import subprocess
import click

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

def get_subscriptions():
  """Fetches Azure subscriptions from CLI."""
  try:
    result = subprocess.run(["az", "account", "list", "--output", "json"], capture_output=True, text=True, check=True)
    subscriptions = json.loads(result.stdout)
    return {sub["name"]: sub["id"] for sub in subscriptions}
  except subprocess.CalledProcessError:
    click.echo("❌ Error: Could not fetch Azure subscriptions. Ensure `az login` is complete.")
    return {}

def switch_subscription(selected_id, selected_name = ""):
    try:
      # Switch to selected subscription
      subprocess.run(["az", "account", "set", "--subscription", selected_id])
      click.echo(f"🔄 Azure subscription switched to: {selected_id} {selected_name}")
    except:
      click.echo(f"❌ Error: Could not switch to subscription: {selected_id} {selected_name}")

def select_subscription():
  """Interactive fuzzy search to select an Azure subscription."""
  sub_dict = get_subscriptions()

  if not sub_dict:
    click.echo("⚠️ No Azure subscriptions found.")
    return

  choices = [f"[{idx+1}]: {name}: {sub_id}" for idx, (name, sub_id) in enumerate(sub_dict.items())]

  # Use `fzf` for fuzzy search
  try:
    result = subprocess.run(["fzf"], input="\n".join(choices), text=True, capture_output=True)
    selected = result.stdout.strip()
  except FileNotFoundError:
    click.echo("❌ Error: `fzf` is not installed. Install it via `brew install fzf` or `sudo apt install fzf`.")
    return

  if selected:
    selected_name = selected.split(":")[1].strip()
    selected_id = sub_dict[selected_name]
    # click.echo(f"✅ Selected: {selected_id}:{selected_name}")
    switch_subscription(selected_id,selected_name)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
  "--subscription","-s", help="Switch to the subscription directly by using the subscription id.", required=False, type=str
)
def main(subscription: str = None) -> None:
  try:
    if subscription is not None:
      switch_subscription(selected_id=subscription)
    else:  
      select_subscription()
  except Exception as e:
    raise e


if __name__ == "__main__":
  main()

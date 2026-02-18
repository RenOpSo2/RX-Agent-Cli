import json
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from gemini_ai import GeminiAI
from brain import process_instructions

console = Console()
ai = GeminiAI()

def main():
    console.print(Panel.fit("[bold magenta]RX-Agent v1.0[/bold magenta]\n[dim]Ready to serve, Bro![/dim]", border_style="magenta"))
    
    while True:
        user_input = console.input("\n[bold green]User[/bold green] : ")
        
        if user_input.lower() in ["exit", "quit", "keluar"]:
            console.print("[yellow]Bye bye, Bro![/yellow]")
            break
            
        with console.status("[bold cyan]Processing...[/bold cyan]"):
            raw_response = ai.ask(user_input)
            
            try:
                data = json.loads(raw_response)
                ai_message = data.get("message", "")
                actions = data.get("actions", [])
                if ai_message:
                    console.print(f"[bold magenta]RX-Agent[/bold magenta]: {ai_message}")
        
                if actions:
                    results = process_instructions(raw_response)
                    for res in results:
                        console.print(Panel(res, title="[dim]Terminal Output[/dim]", border_style="blue"))
                        
            except Exception as e:
                console.print(f"[red]Error parsing brain: {raw_response}[/red]")

if __name__ == "__main__":
    main()


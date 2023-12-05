import rich

def output_classic(args):
    rich.print(f"[bold cyan]{args.title}[/bold cyan]")
    for group in args.groups:
        rich.print(f"[bold blue]{' '*4}- {group['name']}[/bold blue]")
        for test in group["tests"]:
            rich.print(f"[bold magenta]{' '*8}- {test['name']}[/bold magenta]")
            if test.get('ignore'):
                rich.print(f"[bold red]{' '*12}-Test: ignored[/bold red]")
                continue
            if not test['verbose']:
                if test['status']['passed']:
                    rich.print(f"[bold green]{' '*12}-Test: passed[/bold green]")
                else:
                    returned = test['status']['reason']
                    returned = f"'{returned}'" if isinstance(returned, str) else returned
                    rich.print(f"[bold red]{' '*12}-Test: failed: {returned}[/bold red]")
                continue
            if test['params'] != {}:
                rich.print(f"[bold yellow]{' '*12}- inputs:[/bold yellow]")
                for key, value in test['params'].items():
                    value = f"'{value}'" if isinstance(value, str) else value
                    rich.print(f"[bold yellow]{' '*14}- {key}: {value}[/bold yellow]")
            if test.get('instance_params'):
                rich.print(f"[bold yellow]{' '*12}- instance:[/bold yellow]")
                for key, value in test['instance_params'].items():
                    value = f"'{value}'" if isinstance(value, str) else value
                    rich.print(f"[bold yellow]{' '*14}- {key}: {value}[/bold yellow]")
            assert_to = test.get('assert_to', None)
            if not assert_to:
                assert_to_dot = test.get('assert_to_dot', None)
                if not assert_to_dot:
                    rich.print(f"[bold red]{' '*12}-Cannot understand expected.value[/bold red]")
                    rich.print(f"[bold red]{' '*12}-Test: failed[/bold red]")
                    continue
                assert_to_dot = [assert_to_dot[0], ".".join([str(_assert) for _assert in assert_to_dot[1]])]
                assert_to_dot[1] = assert_to_dot[1].replace(';',':')
                assert_to = f"'{assert_to_dot[0]}'; in value.{assert_to_dot[1]}" if isinstance(assert_to_dot[0], str) else f"{assert_to_dot[0]}; in value.{assert_to_dot[1]}"
            else:
                assert_to = f"'{assert_to}'" if isinstance(assert_to, str) else assert_to
            returned = test['status']['reason']
            returned = f"'{returned}'" if isinstance(returned, str) else returned
            
            rich.print(f"[bold yellow]{' '*12}- assertion: {test['assertion']}[/bold yellow]")
            rich.print(f"[bold yellow]{' '*12}- assert to: {assert_to}[/bold yellow]")
            rich.print(f"[bold yellow]{' '*12}- returned: {returned}[/bold yellow]")
            if test['status']['passed']:
                rich.print(f"[bold green]{' '*12}-Test: passed[/bold green]")
            else:
                rich.print(f"[bold red]{' '*12}-Test: failed[/bold red]")
litio = {
    'output': {
        'litio': output_classic
    }
}
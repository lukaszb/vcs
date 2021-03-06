from vcs.cli import ChangesetCommand
from vcs.cli import make_option


class LogCommand(ChangesetCommand):
    TEMPLATE = u'{cs.raw_id} | {cs.date} | {cs.author} | {cs.message}'

    option_list = ChangesetCommand.option_list + (
        make_option('-t', '--template', action='store', dest='template',
            default=TEMPLATE,
            help=(
                'Specify own template. Default is: "{default_template}"'.format(
                default_template=TEMPLATE)),
        ),
        make_option('-p', '--patch', action='store_true', dest='show_patches',
            default=False, help='Show patches'),
    )

    def get_last_commit(self, repo, cid=None):
        return repo.get_changeset(cid)

    def get_template(self, **options):
            return options.get('template', self.TEMPLATE)

    def handle_changeset(self, changeset, **options):
        template = self.get_template(**options)
        output = template.format(cs=changeset)
        output = u'{output}\n'.format(output=output)
        self.stdout.write(output)


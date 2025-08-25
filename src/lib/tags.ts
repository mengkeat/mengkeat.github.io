import { getCollection } from 'astro:content';

export type TagInfo = {
  tag: string;
  count: number;
  slug: string;
};

/** Simple slugify for tag URLs (kebab-case, ascii-safe) */
export function slugify(tag: string) {
  return tag
    .toLowerCase()
    .trim()
    .replace(/\s+/g, '-')
    .replace(/[^\w-]/g, '')
    .replace(/-+/g, '-');
}

/** Aggregate tags across content collections (blog + til) */
export async function collectTags(): Promise<TagInfo[]> {
  const collections = ['blog', 'til'] as const;
  const counts = new Map<string, number>();

  for (const col of collections) {
    const items = await getCollection(col);
    for (const item of items) {
      const tags: string[] = (item.data as any).tags ?? [];
      for (const raw of tags) {
        const tag = String(raw).trim();
        if (!tag) continue;
        counts.set(tag, (counts.get(tag) ?? 0) + 1);
      }
    }
  }

  const result: TagInfo[] = Array.from(counts.entries()).map(([tag, count]) => ({
    tag,
    count,
    slug: slugify(tag),
  }));

  // Sort by count desc, then alphabetically
  result.sort((a, b) => (b.count - a.count) || a.tag.localeCompare(b.tag));
  return result;
}
